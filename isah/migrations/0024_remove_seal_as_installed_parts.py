# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-09-17 18:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('isah', '0023_auto_20160917_1642'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seal',
            name='as_installed_parts',
        ),
    ]