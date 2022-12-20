from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, FormView

from apps.forms import LoginForm, RegisterForm, UserPasswordChangeForm, ForgotPasswordForm, ResetPasswordForm
from apps.models import User
from apps.task.tasks import send_email
from apps.utils.token import account_activation_token


class RegisterView(CreateView):  # NOQA
    template_name = 'apps/auth/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user:
            user = authenticate(username=form.data['username'], password=form.data['password1'])
            if user:
                login(self.request, user)
        current_site = get_current_site(self.request)
        send_email.apply_async(args=[form.data.get('email'), current_site.domain])
        return super().form_valid(form)

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('login')
        return super().get(request, *args, **kwargs)

    # def form_invalid(self, form):
    #     return super().form_invalid(form)


class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('index_page')
    template_name = 'apps/auth/register.html'


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'apps/auth/login.html'
    next_page = reverse_lazy('index_page')


class UserTemplateView(TemplateView):  # NOQA
    template_name = 'apps/auth/user.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = User.objects.filter(username=kwargs.get('username')).first()
        return context


class UserUpdateView(UpdateView, LoginRequiredMixin):
    model = User
    fields = ('username', 'first_name', 'last_name', 'email', 'phone',
              'about', 'workspace', 'address', 'birthday', 'gender',
              'facebook_url', 'instagram_url', 'twitter_url', 'dribbble_url',
              )
    template_name = 'apps/auth/user_update.html'
    success_url = reverse_lazy('user_view')


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('index_page')
    template_name = 'apps/auth/delete_confirm.html'


class UserActiveProfileView(TemplateView):
    template_name = 'apps/auth/email/email_activation.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            user = None
        if user and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request=request, level=messages.SUCCESS, message='Your profile is active')
            return redirect('index_page')
        else:
            return HttpResponse("URL is already invalid")


class UserChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'apps/auth/user_change_password.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('user_view')

    def post(self, request, *args, **kwargs):
        user = self.request.user
        old_password = self.request.POST.get('old_password')
        new_password = self.request.POST.get('new_password1')
        confirm_password = self.request.POST.get('new_password2')

        # pbkdf2_sha256$390000$y72BUFUIWi00JNCcBjUpDu$uU5RqXR59XC2yqN0tJLT + YVsv8sVAFfvMntf6aZjZcY =

        if user.check_password(old_password) and new_password == confirm_password:
            user.set_password(new_password)
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(request=request, level=messages.SUCCESS, message='Your password was changed')
            return redirect('user_view', username=user.username)
        return HttpResponse('Error was found , please fill blanks correct')


class ForgotPasswordFormView(FormView):
    template_name = 'apps/forgot_password.html'
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('reset_password')

    def form_valid(self, form):
        url = get_current_site(self.request)
        send_email.apply_async(args=[form.data.get('email'), url.domain, 'reset'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ResetPasswordView(FormView):
    template_name = 'apps/reset_password.html'
    form_class = ResetPasswordForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['uid'] = self.kwargs.get('uid')
        context['token'] = self.kwargs.get('token')
        return context

    def get_user(self, uid, token):
        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(id=uid)
        except Exception as e:
            user = None
        return user, user and account_activation_token.check_token(user, token)

    def get(self, request, *args, **kwargs):
        user, is_valid = self.get_user(**kwargs)
        if not is_valid:
            return HttpResponse('Link not Found')
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        user, is_valid = self.get_user(**kwargs)
        if is_valid:
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                return redirect('login')
        return HttpResponse('Link not found 404')
