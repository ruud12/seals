# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 08:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0024_auto_20160629_1032'),
    ]

    operations = [
        migrations.AddField(
            model_name='supremeadvise',
            name='aft',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sealadvisor2.AftSealOptions'),
        ),
    ]
