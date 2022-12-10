from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse, path
from django.utils.html import format_html

from apps.models import Category, Post, Comment


@admin.register(Category)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('name', 'posts_count',)
    exclude = ('slug',)

    def posts_count(self, obj):  # NOQA
        return obj.post_set.count()


@admin.register(Post)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('id', 'categories_list', 'title', 'is_active', 'category_image', 'submit_buttons')
    exclude = ('slug', 'views')
    search_fields = ['category__name']
    change_form_template = "admin/custom/change_form.html"

    def is_active(self, obj: Post):  # NOQA
        data = {
            'pending': '<i class="fa-solid fa-hourglass-start" style="color: grey; font-size: 1em;margin-top: 8px; margin: auto;"></i>',
            # noqa
            'active': '<i class="fa-solid fa-check" style="color: green; font-size: 1em;margin-top: 8px; margin: auto;"></i>',
            # noqa
            'cancel': '<i class="fa-solid fa-circle-xmark"  style="color: red; font-size: 1em;margin-top: 8px; margin: auto;"></i>'
            # noqa
        }
        return format_html(data[obj.status])

    def categories_list(self, obj):  # NOQA
        ls = []
        for i in obj.category.all():
            ls.append(f'''<a href="{reverse('admin:apps_category_change', args=(i.pk,))}">{i.name}</a>''')
        return format_html(' ,'.join(ls))

    def get_urls(self):
        urls = super().get_urls()
        my_urls = [path('active/<int:id>', self.active),
                   path('cancel/<int:id>', self.cancel)]
        return urls + my_urls

    def response_change(self, request, obj):
        if "_active" in request.POST:
            obj.status = Post.StatusChoise.ACTIVE
            obj.save()
            self.message_user(request, "Post was activated")
            return HttpResponseRedirect("../")
        elif "_cancel" in request.POST:
            obj.status = Post.StatusChoise.CANCEL
            obj.save()
            self.message_user(request, "Post was deactivated")
            return HttpResponseRedirect("../")
        if "_make_pdf" in request.POST:
            pass
        elif "_post_view" in request.POST:
            return redirect(f'post_preview_page', obj.slug)
        return super().response_change(request, obj)

    def active(self, request, id):
        post = Post.objects.filter(id=id).first()
        post.status = Post.StatusChoise.ACTIVE
        post.save()
        return HttpResponseRedirect('../')

    def cancel(self, request, id):
        post = Post.objects.filter(id=id).first()
        post.status = Post.StatusChoise.CANCEL
        post.save()
        return HttpResponseRedirect('../')

    def category_count(self, obj):  # NOQA
        return obj.category.count()

    def category_image(self, obj):  # NOQA
        return format_html(f'<img style="border-radius: width="110px" height="50px"" src="{obj.image.url}" />')


@admin.register(Comment)
class OriginAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'text')
    exclude = ('slug',)
