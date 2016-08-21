# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-21 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isah', '0019_auto_20160821_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicereport',
            name='vessel',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='isah.SealVessel', verbose_name='Serviced vessel'),
            preserve_default=False,
        ),
    ]
