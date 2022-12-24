from base64 import b64encode
from datetime import date
from io import BytesIO

from django.contrib.sites.shortcuts import get_current_site
from django.db.models import Count
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import TemplateView, ListView, FormView
from qrcode import make

from apps.forms import ContactForm
from apps.models import Category, Post, ContactInfo, ContactMessage
from apps.utils.make_pdf import render_to_pdf  # created in step 4


class SearchView(View):
    def post(self, request, *args, **kwargs):
        like = request.POST.get('like')
        data = {
            'posts': list(Post.objects.filter(title__icontains=like).values('title', 'image', 'slug')),
            'domain': get_current_site(request).domain
        }
        return JsonResponse(data)


class IndexView(ListView):
    queryset = Post.active.all()
    context_object_name = 'posts__category'
    template_name = 'apps/index.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context['posts'] = Post.active.all()[1:]
        context['categories'] = Category.objects.all().annotate(article_count=
                                                                Count('post_set')).order_by('-article_count')[:4]
        context['treading_post'] = Post.active.order_by('-views')[:5]
        return context


class BlogCategoryListView(ListView):
    queryset = Post.active.all()
    template_name = 'apps/blog-category.html'
    paginate_by = 4

    # context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        slug = self.request.GET.get('category')
        context['categories'] = Category.objects.all()
        context['posts'] = self.get_queryset()
        context['category'] = Category.objects.filter(slug=slug).first()
        context['treading_post'] = Post.active.order_by('-views')[:5]

        return context

    def get_queryset(self):
        qs = super().get_queryset()
        if category := self.request.GET.get('category'):
            return qs.filter(category__slug=category)
        return qs


class AboutView(TemplateView):
    template_name = 'apps/about.html'


class ContactView(FormView):
    model = ContactMessage
    template_name = 'apps/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['info'] = ContactInfo.objects.all().first()
        return context

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        return redirect('contact_page')

    def form_invalid(self, form):
        return super().form_invalid(form)


class GeneratePdf(View):

    def get(self, request, *args, **kwargs):
        post = Post.objects.get(slug=kwargs.get('slug'))
        url = request.build_absolute_uri(reverse('post_page', kwargs={'slug': self.kwargs.get('slug')}))

        qr_rend = BytesIO()

        img = make(url)
        img.save(qr_rend)
        dataurl = 'data:image/png;base64,' + b64encode(qr_rend.getvalue()).decode('ascii')

        data = {
            'post': post,
            'today': date.today(),
            'qr': dataurl,
            'img': img,
        }
        pdf = render_to_pdf('make_pdf.html', data)
        return HttpResponse(pdf, content_type='application/pdf')
