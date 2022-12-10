from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView, DetailView, CreateView, FormView

from apps.forms import LoginForm, RegisterForm, CommentForm, CreatePostForm
from apps.models import Category, Post, Comment


class RegisterView(CreateView):
    template_name = 'apps/auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('index_page')

    def form_valid(self, form):
        # form.instance.is_active = False
        data = {
            'username': form.data['username'],
            'email': form.data['password1']
        }
        user = form.save()
        # user = authenticate(username=form.data['username'], password=form.data['password1'])
        if user:
            login(self.request, user)
        return redirect('index_page')

    def form_invalid(self, form):
        return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index_page')
    template_name = 'apps/auth/register.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'apps/auth/login.html'
    next_page = reverse_lazy('index_page')


class IndexView(ListView):
    queryset = Post.objects.filter(status='active').order_by('-created_at')
    context_object_name = 'posts__category'
    template_name = 'apps/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['posts'] = Post.objects.filter(status='active').order_by('-created_at')[1:]
        context['categories'] = Category.objects.all().annotate(article_count=
                                                                Count('post_set')).order_by('-article_count')[:4]
        context['treading_post'] = Post.objects.filter(status='active').order_by('-views')[:5]
        return context


class BlogCategoryListView(ListView):
    queryset = Post.objects.filter(status='active')
    template_name = 'apps/blog-category.html'
    paginate_by = 4
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        slug = self.request.GET.get('category')
        context['categories'] = Category.objects.all()
        context['posts'] = self.get_queryset()
        context['category'] = Category.objects.filter(slug=slug).first()
        context['treading_post'] = Post.objects.filter(status='active').order_by('-views')[:5]

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class PostDetailView(DetailView, FormView):
    model = Post
    context_object_name = 'post'
    template_name = 'apps/post.html'
    form_class = CommentForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views = obj.views + 1
        return obj

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['comments'] = Comment.objects.filter(post_id=self.get_object().id)
        return contex

    def form_valid(self, form):
        _object = self.get_object()
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.post = _object
        obj.save()
        return redirect('post_page', slug=_object.slug)

    def form_invalid(self, form):
        return super().form_invalid(form)


class PostUpdate(DetailView):
    model = Post
    template_name = 'apps/post_preview.html'
    context_object_name = 'post'

    def post(self, request, *args, **kwargs):
        post = self.get_object()
        post.status = self.request.POST.get('status')
        post.save()
        return HttpResponseRedirect(reverse('admin:apps_post_change', args=(post.pk,)))


class ContactView(TemplateView):
    template_name = 'apps/contact.html'


class AboutView(TemplateView):
    template_name = 'apps/about.html'


class UserView(LoginRequiredMixin, TemplateView):
    template_name = 'apps/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class CreatePostView(CreateView):
    template_name = 'apps/add-post.html'
    model = Post
    form_class = CreatePostForm
    success_url = reverse_lazy('index_page')

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['categories'] = Category.objects.all()
        return contex

    def form_valid(self, form):
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
