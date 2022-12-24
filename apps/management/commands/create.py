import csv

from django.core.management.base import BaseCommand

from apps.models import Region, District


class Command(BaseCommand):
    help = 'Creating region or district table'

    def add_arguments(self, parser):
        parser.add_argument('type', type=str, help='Choose region or district')

    def handle(self, *args, **options):
        choose = options.get('type')
        if choose == 'region':
            with open('apps/static/files/regions.csv', 'r') as f:
                f.readline()
                read = csv.reader(f)
                for row in read:
                    _str_name, was_created = Region.objects.get_or_create(
                        id=row[0],
                        name=row[1]
                    )
        elif choose == 'district':
            with open('apps/static/files/districts.csv', 'r') as f:
                f.readline()
                read = csv.reader(f)
                for row in read:
                    _str_name, was_created = District.objects.get_or_create(
                        id=row[0],
                        name=row[1],
                        region_id=row[2]
                    )
