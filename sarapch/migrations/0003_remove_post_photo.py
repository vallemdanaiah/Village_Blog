# Generated by Django 4.0 on 2024-02-23 09:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sarapch', '0002_post_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
