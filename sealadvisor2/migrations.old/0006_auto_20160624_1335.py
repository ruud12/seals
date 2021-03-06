# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-24 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sealadvisor2', '0005_auto_20160624_1202'),
    ]

    operations = [
        migrations.CreateModel(
            name='supremeAftShaftInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aft_shaft_size', models.IntegerField(blank=True, null=True, verbose_name='Aft shaft diameter (mm)')),
                ('aft_pcd_liner', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Aft seal liner PCD [mm]')),
                ('aft_pcd_flange', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Aft seal flange ring PCD [mm]')),
                ('aft_centering_edge', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Aft seal flange ring centering edge [mm]')),
            ],
        ),
        migrations.CreateModel(
            name='supremeFwdShaftInformation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fwd_shaft_size', models.IntegerField(blank=True, null=True, verbose_name='Forward shaft diameter (mm)')),
                ('fwd_pcd_liner', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='forward seal liner PCD [mm]')),
                ('fwd_pcd_flange', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='forward seal flange PCD [mm]')),
                ('fwd_centering_edge', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='forward seal centering edge [mm]')),
            ],
        ),
        migrations.AddField(
            model_name='supremeadvise',
            name='draught_shaft',
            field=models.DecimalField(decimal_places=1, default=1, max_digits=5, verbose_name='Shaft centerline draught (m)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='supremeadvise',
            name='rpm',
            field=models.IntegerField(default=1, verbose_name='Shaft rotational speed (RPM)'),
            preserve_default=False,
        ),
    ]
