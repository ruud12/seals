# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-28 15:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0020_auto_20160628_1722'),
    ]

    operations = [
        migrations.AddField(
            model_name='supremeadvise',
            name='aftSize',
            field=models.DecimalField(blank=True, decimal_places=1, default=1, max_digits=5, verbose_name='Aft shaft diameter (mm)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supremeadvise',
            name='fwdSize',
            field=models.DecimalField(blank=True, decimal_places=1, default=1, max_digits=5, verbose_name='Forward shaft diameter (mm)'),
            preserve_default=False,
        ),
    ]
