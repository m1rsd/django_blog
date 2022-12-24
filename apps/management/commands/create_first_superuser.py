from django.core.management.base import BaseCommand

from django.core.management.base import BaseCommand

from apps.models import User


class Command(BaseCommand):
    help = 'Creating region or district table'

    def handle(self, *args, **options):
        User.objects.create_user(
            username='admin',
            email='',
            is_active=1,
            is_staff=1,
            password='1'
        )