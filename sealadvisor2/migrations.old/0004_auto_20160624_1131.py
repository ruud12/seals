# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 09:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0003_auto_20160624_1123'),
    ]

    operations = [
        migrations.AddField(
            model_name='sealadvisorwizard',
            name='aft_seal',
            field=models.BooleanField(default=False, verbose_name='Aft seal required?'),
        ),
        migrations.AddField(
            model_name='sealadvisorwizard',
            name='fwd_seal',
            field=models.BooleanField(default=False, verbose_name='Forward seal required?'),
        ),
    ]
