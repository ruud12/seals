# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor', '0018_auto_20160623_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advise',
            name='type_approval',
            field=models.CharField(blank=True, max_length=200, verbose_name='Type approval required (specify which or leave blank)'),
        ),
    ]
