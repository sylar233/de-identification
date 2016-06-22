# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-21 10:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False)),
                ('task_name', models.CharField(max_length=100)),
                ('data_path', models.CharField(max_length=300)),
                ('selected_attrs', models.TextField(max_length=500)),
                ('jtree_strct', models.TextField(max_length=500)),
                ('dep_graph', models.TextField()),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(blank=True)),
                ('status', models.PositiveSmallIntegerField(choices=[(0, 'WAITTING'), (1, 'FINISH'), (2, 'ERROR')], default=0)),
            ],
            options={
                'ordering': ('create_time',),
            },
        ),
    ]
