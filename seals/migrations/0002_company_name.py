# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-23 18:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seals', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='name',
            field=models.CharField(default=1, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
    ]
