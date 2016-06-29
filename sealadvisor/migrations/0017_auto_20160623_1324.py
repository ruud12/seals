# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-23 11:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor', '0016_auto_20160623_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='advise',
            name='fkm_forward',
            field=models.BooleanField(default=False, verbose_name='FKM lip seals'),
        ),
        migrations.AddField(
            model_name='advise',
            name='hml_forward',
            field=models.BooleanField(default=False, verbose_name='HML wear resistant liner coating'),
        ),
        migrations.AddField(
            model_name='advise',
            name='ocr',
            field=models.BooleanField(default=False, verbose_name='Oil collector ring'),
        ),
        migrations.AlterField(
            model_name='advise',
            name='netcutters',
            field=models.CharField(choices=[('no', 'No netcutter'), ('clockwise', 'Clockwise'), ('counterclockwise', 'Counterclockwise'), ('two', 'Two of each on one seal')], default='no', max_length=30),
        ),
    ]