# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 11:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0007_auto_20160624_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='supremeadvise',
            name='aft_seal_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sealadvisor2.supremeAftShaftInformation'),
        ),
        migrations.AddField(
            model_name='supremeadvise',
            name='fwd_seal_information',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sealadvisor2.supremeFwdShaftInformation'),
        ),
    ]
