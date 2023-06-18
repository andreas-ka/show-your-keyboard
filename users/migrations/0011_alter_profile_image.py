# Generated by Django 3.2.19 on 2023-06-18 12:44

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_alter_profile_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format='WEBP', keep_meta=True, null=True, quality=100, scale=None, size=[90, 90], upload_to='profiles/'),
        ),
    ]