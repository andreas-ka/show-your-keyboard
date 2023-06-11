# Generated by Django 3.2.19 on 2023-06-11 19:40

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230611_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(crop=None, force_format='WEBP', keep_meta=True, quality=75, scale=None, size=[100, 100], upload_to='profiles/'),
        ),
    ]
