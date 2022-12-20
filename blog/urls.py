from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog import settings

# from apps.admin import event_admin_site

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('event-admin/', event_admin_site.urls),
    path('', include('apps.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
