# Generated by Django 2.2.1 on 2019-09-23 11:23

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('basic_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserProfileInfor',
            new_name='UserProfileInfo',
        ),
    ]