# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-17 06:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isah', '0015_auto_20160817_0802'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicereport',
            name='remarks',
            field=models.CharField(blank=True, max_length=2000, verbose_name='Remarks'),
        ),
    ]
