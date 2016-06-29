# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 12:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor', '0022_auto_20160623_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advise',
            name='netcutters',
            field=models.BooleanField(default=False, verbose_name='Netcutters?'),
        ),
        migrations.AlterField(
            model_name='advise',
            name='sandy',
            field=models.BooleanField(default=False, verbose_name='Will the seal be applied in a sandy/dirty environment?'),
        ),
    ]