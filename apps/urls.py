from django.urls import path

from apps.views import IndexView, BlogCategoryListView, ContactView, AboutView, PostDetailView, CustomLoginView, \
    CustomLogoutView, RegisterView, UserView, PostUpdate, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post_page'),
    path('preview-post/<str:slug>', PostUpdate.as_view(), name='post_preview_page'),
    path('blog-category/', BlogCategoryListView.as_view(), name='blog_category_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),

    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register_view'),
    path('user/', UserView.as_view(), name='user_view')

]
