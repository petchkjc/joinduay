# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-05-08 10:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_act',
            name='description',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
    ]
