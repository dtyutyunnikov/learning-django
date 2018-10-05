# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-10-05 10:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='added_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='answer',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='added_at',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='question',
            name='rating',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='question',
            name='likes',
            field=models.ManyToManyField(related_name='like', to=settings.AUTH_USER_MODEL),
        ),
    ]
