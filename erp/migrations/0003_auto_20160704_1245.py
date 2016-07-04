# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-04 10:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0002_confirmcomponentchange'),
    ]

    operations = [
        migrations.AddField(
            model_name='confirmcomponentchange',
            name='new_part',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='new_part', to='erp.Part'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='confirmcomponentchange',
            name='old_part',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='old_part', to='erp.Part'),
        ),
    ]
