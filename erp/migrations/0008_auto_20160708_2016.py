# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-08 18:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_auto_20160708_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vessel',
            name='contacts',
            field=models.ManyToManyField(blank=True, to='erp.contactPerson'),
        ),
    ]