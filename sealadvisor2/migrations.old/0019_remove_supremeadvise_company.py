# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 15:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0018_auto_20160628_0901'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supremeadvise',
            name='company',
        ),
    ]