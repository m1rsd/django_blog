from celery import shared_task
from django.core.mail import send_mail, EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode

from apps.models import User
from apps.utils.token import account_activation_token
from blog.settings import EMAIL_HOST_USER


@shared_task
def send_email_celery(user, recipient_list):
    text = f'Thank you {user} for your message.\nWe will fix this problem as soon as possible!'
    subject = 'Answer Email'
    from_email = EMAIL_HOST_USER
    recipient_list = [recipient_list]
    result = send_mail(subject, text, from_email, recipient_list)
    return result


@shared_task
def send_email(email, domain, type_email='active'):
    user = User.objects.filter(email=email).first()
    context = {
        'user': user,
        'domain': domain,
        'uid': urlsafe_base64_encode(force_bytes(str(user.pk))),
        'token': account_activation_token.make_token(user)
    }
    subject = 'Active your account'
    template = 'email_activation.html'
    if type_email == 'reset':
        subject = "Do you have a trouble with your password?"
        template = 'reset_password.html'
    elif type_email == 'change':
        pass
    else:
        context['username'] = user.username
    message = render_to_string(f'apps/auth/email/{template}', context)
    recipient_list = [email]

    email = EmailMessage(subject, message, EMAIL_HOST_USER, recipient_list)
    email.content_subtype = 'html'
    result = email.send()
    return result
