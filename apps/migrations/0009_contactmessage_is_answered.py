# Generated by Django 4.1.3 on 2022-12-11 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0008_contactmessage_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactmessage',
            name='is_answered',
            field=models.BooleanField(default=False, verbose_name='Is Answered'),
        ),
    ]
