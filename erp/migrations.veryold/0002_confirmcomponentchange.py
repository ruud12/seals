# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 10:06
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='confirmComponentChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_part', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.Part')),
                ('report', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.serviceReport')),
            ],
        ),
    ]
