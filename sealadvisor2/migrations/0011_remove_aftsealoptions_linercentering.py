# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 07:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0010_auto_20160728_0906'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aftsealoptions',
            name='linerCentering',
        ),
    ]