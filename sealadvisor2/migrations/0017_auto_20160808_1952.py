# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-08 17:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0016_supremeadvise_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supremeadvise',
            name='linerCentering',
            field=models.CharField(choices=[('shaft', 'Shaft centered'), ('hub', 'Hub centered')], max_length=20, verbose_name='Liner centering'),
        ),
    ]
