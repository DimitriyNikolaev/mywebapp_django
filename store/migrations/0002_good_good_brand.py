# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-24 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='good',
            name='good_brand',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
