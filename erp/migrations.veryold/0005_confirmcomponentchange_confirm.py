# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_confirmcomponentchange_seal'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmcomponentchange',
            name='confirm',
            field=models.BooleanField(default=False),
        ),
    ]
