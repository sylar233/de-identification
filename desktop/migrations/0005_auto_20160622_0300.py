# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-22 03:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('desktop', '0004_job'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='synthetic_path',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
