from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.core.mail import send_mail
from django.forms import ModelForm, Form, EmailField, CharField

from apps.models import User, Post, Comment, ContactMessage


class LoginForm(AuthenticationForm):
    pass


class UserPasswordChangeForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ('password',)


class ForgotPasswordForm(Form):
    email = EmailField()

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not User.objects.filter(email=email).exists():
            raise ValidationError('This profile is not registered')
        return email

    class Meta:
        model = User
        fields = ('email',)


class ResetPasswordForm(Form):
    new_password1 = CharField(max_length=128)
    new_password2 = CharField(max_length=128)

    def clean_new_password1(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 != password2:
            raise ValidationError('Confirm password is incorect')
        return password1

    class Meta:
        model = User


class Meta:
    model = User
    fields = ('email',)


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone',
                  'about', 'workspace', 'address', 'birthday', 'gender',
                  'facebook_url', 'instagram_url', 'twitter_url', 'dribbble_url',
                  )


class ContactForm(ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['title', 'text', 'email']


class CreatePostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'image', 'content', 'category']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)


class RegisterForm(UserCreationForm):
    phone = CharField(max_length=25)

    def clean_phone(self):
        phone = self.data.get('phone').replace('(', '')
        phone = phone.replace(')', '')
        phone = phone.replace('-', '')
        phone = phone.replace(' ', '')
        return phone

    class Meta:
        model = User
        fields = ("username", "email", "phone", "password1")


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ('status',)
