from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.forms import ModelForm

from apps.models import User, Post, Comment


class LoginForm(AuthenticationForm):
    pass


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1")


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('status',)
