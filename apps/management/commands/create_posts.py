from django.core.management import BaseCommand
from faker import Faker
from faker.utils.text import slugify

from apps.models import Post


class Command(BaseCommand):
    help = 'Create some posts'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='total count of creating posts')

    def handle(self, *args, **options):
        total = options.get('total')
        faker = Faker()
        for i in range(total):
            _str_name, was_created = Post.objects.get_or_create(
                title=faker.sentence(100),
                slug=slugify(faker.text(100)),
                content=faker.text(1000),
                author_id=1,
                status=Post.StatusChoise.ACTIVE,
                created_at=faker.date_time_between_dates()
            )
