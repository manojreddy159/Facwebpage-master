# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-21 00:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fac', '0030_auto_20171119_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='experience',
            name='year',
            field=models.CharField(default=b'', max_length=100),
        ),
    ]
