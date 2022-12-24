from builtins import next

from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from apps.view.user_views import CustomLogoutView, RegisterView, UserListView, CustomLoginView, UserUpdateView, \
    UserDeleteView, UserActiveProfileView, UserChangePasswordView, ForgotPasswordFormView, ResetPasswordView, \
    UserPostListView
from apps.view.views import IndexView, BlogCategoryListView, ContactView, AboutView, GeneratePdf, SearchView
from apps.view.post_views import PostDetailView, PostUpdate, CreatePostView

urlpatterns = [
    path('', IndexView.as_view(), name='index_page'),
    path('post/<str:slug>', PostDetailView.as_view(), name='post_page'),
    path('preview-post/<str:slug>', PostUpdate.as_view(), name='post_preview_page'),
    path('blog-category/', BlogCategoryListView.as_view(), name='blog_category_page'),
    path('contact/', ContactView.as_view(), name='contact_page'),
    path('about/', AboutView.as_view(), name='about_page'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('pdf/<str:slug>', GeneratePdf.as_view(), name='make_pdf'),

    path('search', csrf_exempt(SearchView.as_view()), name='search'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register_view'),
    path('channge_password/', UserChangePasswordView.as_view(), name='change_password'),
    path('forgot_password/', ForgotPasswordFormView.as_view(), name='forgot_password'),
    path('reset/<str:uid>/<str:token>', ResetPasswordView.as_view(), name='reset_password'),
    path('activate/<str:uid>/<str:token>', UserActiveProfileView.as_view(), name='confirm_email'),
    path('user/<str:username>', UserListView.as_view(), name='user_view'),
    path('<str:username>/posts', UserPostListView.as_view(), name='user_posts'),
    path('update/user/<int:pk>', UserUpdateView.as_view(), name='user_update_view'),
    path('delete/user/<int:pk>', UserDeleteView.as_view(), name='user_delete_view'),

]
