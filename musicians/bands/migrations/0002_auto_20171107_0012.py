# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-07 00:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bands', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='band',
            name='twitter_id',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
