# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-13 07:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0004_remove_supremeadvise_fwd_build_in_length'),
    ]

    operations = [
        migrations.AddField(
            model_name='supremeadvise',
            name='vgp',
            field=models.BooleanField(default=False, verbose_name='Has to comply with VGP regulations'),
        ),
    ]
