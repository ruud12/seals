# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-29 08:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0022_auto_20160629_0844'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='supremeadvise',
            name='aft_shaft_information',
        ),
        migrations.RemoveField(
            model_name='supremeadvise',
            name='environmental',
        ),
        migrations.RemoveField(
            model_name='supremeadvise',
            name='fwd_shaft_information',
        ),
        migrations.DeleteModel(
            name='environmentalInformation',
        ),
        migrations.DeleteModel(
            name='supremeAftShaftInformation',
        ),
        migrations.DeleteModel(
            name='supremeFwdShaftInformation',
        ),
    ]
