# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-16 11:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isah', '0008_auto_20160815_1831'),
    ]

    operations = [
        migrations.CreateModel(
            name='LS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('LS_number', models.CharField(max_length=10, verbose_name='LS number')),
                ('description', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Description')),
                ('seals', models.ManyToManyField(to='isah.Seal', verbose_name='Related seals')),
            ],
        ),
    ]
