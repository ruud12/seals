# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-30 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0031_aftsealoptions_air'),
    ]

    operations = [
        migrations.CreateModel(
            name='FwdSealOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocr', models.BooleanField(default=False, verbose_name='OCR ring')),
                ('fkm', models.BooleanField(default=False, verbose_name='Use FKM lip-seals')),
            ],
        ),
    ]