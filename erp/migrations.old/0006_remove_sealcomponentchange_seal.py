# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-03 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0005_sealcomponentchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sealcomponentchange',
            name='seal',
        ),
    ]
