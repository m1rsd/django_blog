# Generated by Django 4.1.3 on 2022-12-16 11:25

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('apps', '0009_contactmessage_is_answered'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='active'),
        ),
    ]
