# Generated by Django 4.1.3 on 2022-12-01 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_alter_comment_text_alter_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('pending', 'Kutilmoqda'), ('active', 'Activlashgan'), ('cancel', 'Rad etilgan')], default='pending', max_length=55),
        ),
    ]