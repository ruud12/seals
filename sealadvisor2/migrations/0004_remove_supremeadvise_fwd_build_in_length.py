# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 07:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0003_auto_20160712_1144'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supremeadvise',
            name='fwd_build_in_length',
        ),
    ]