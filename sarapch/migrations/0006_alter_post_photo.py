# Generated by Django 4.0 on 2024-02-23 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarapch', '0005_alter_post_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.ImageField(upload_to=''),
        ),
    ]
