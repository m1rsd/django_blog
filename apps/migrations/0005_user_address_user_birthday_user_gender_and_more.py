# Generated by Django 4.1.3 on 2022-12-08 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0004_alter_user_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='birthday',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='gender',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='workspace',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
