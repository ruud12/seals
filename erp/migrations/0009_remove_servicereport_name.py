# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-10 11:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0008_auto_20160708_2016'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='servicereport',
            name='name',
        ),
    ]