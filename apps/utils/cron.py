import datetime
import os

import django
from apps.models import Post

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
django.setup()


def view_count_reseter():
    date = datetime.date.today()
    date_delta = datetime.timedelta(7)
    Post.objects.filter(created_at__lt=date - date_delta, status=Post.StatusChoise.CANCEL).delete()
