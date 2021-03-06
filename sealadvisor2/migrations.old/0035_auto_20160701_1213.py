# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-01 10:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0034_environmentaloptions_oiltype'),
    ]

    operations = [
        migrations.AddField(
            model_name='supremeadvise',
            name='pressure_oring',
            field=models.BooleanField(default=False, verbose_name='Pressure O-ring'),
        ),
        migrations.AlterField(
            model_name='environmentaloptions',
            name='air',
            field=models.BooleanField(default=False, verbose_name='Use an air type system (Ventus/Athmos) to comply with VGP and reduce the pressure on the lip seals (only aft seal)'),
        ),
    ]
