# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0009_auto_20180919_1155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='plan',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
