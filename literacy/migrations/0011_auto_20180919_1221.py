# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 09:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0010_auto_20180919_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stkpush_call_back',
            name='result_description',
            field=models.TextField(blank=True),
        ),
    ]
