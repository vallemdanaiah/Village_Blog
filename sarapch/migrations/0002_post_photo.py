# Generated by Django 4.0 on 2024-02-23 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sarapch', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default='.jpg', upload_to='media'),
            preserve_default=False,
        ),
    ]
