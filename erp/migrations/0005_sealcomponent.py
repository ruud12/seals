# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 17:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0004_auto_20160702_1904'),
    ]

    operations = [
        migrations.CreateModel(
            name='sealComponent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Part')),
            ],
        ),
    ]
