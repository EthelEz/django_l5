# Generated by Django 2.2.5 on 2019-09-26 21:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20190926_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.AddField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 26, 21, 58, 44, 679173, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
