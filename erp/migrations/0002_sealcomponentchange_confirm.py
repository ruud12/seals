# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 09:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sealcomponentchange',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
