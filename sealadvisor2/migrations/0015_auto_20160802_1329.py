# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 11:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0014_auto_20160801_0748'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aftsealoptions',
            name='anode',
            field=models.BooleanField(default=False, verbose_name='Cathodic protection'),
        ),
    ]
