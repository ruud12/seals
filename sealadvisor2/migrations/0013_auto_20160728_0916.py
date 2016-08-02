# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-28 07:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0012_fwdsealoptions_high_pressure'),
    ]

    operations = [
        migrations.AddField(
            model_name='fwdsealoptions',
            name='hml',
            field=models.BooleanField(default=False, verbose_name='Hard metal layer (HML)'),
        ),
        migrations.AlterField(
            model_name='fwdsealoptions',
            name='high_pressure',
            field=models.BooleanField(default=False, verbose_name='High pressure (3 lip-seals)'),
        ),
    ]