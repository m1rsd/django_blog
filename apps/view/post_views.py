from django.db.models import Count
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, FormView

from apps.forms import CommentForm, CreatePostForm
from apps.models import Category, Post, Comment, PostViews


class PostDetailView(DetailView, FormView):
    model = Post
    context_object_name = 'post'
    template_name = 'apps/post.html'
    form_class = CommentForm

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views = (PostViews.objects.filter(post=obj.id).annotate(dcount=Count('post'))).count()
        obj.save()
        PostViews.objects.create(post=obj)
        return obj

    def get_context_data(self, **kwargs):
        contex = super().get_context_data(**kwargs)
        contex['comments'] = Comment.objects.filter(post_id=self.get_object().id)
        return contex

    def post(self, request, *args, **kwargs):
        if "_make_pdf" in request.POST:
            return redirect('make_pdf', self.get_object().slug)
        return super().post(request, *args, **kwargs)

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
        post = form.save(commit=False)
        post.author = self.request.user
        post.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
