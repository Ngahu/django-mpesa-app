# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0012_auto_20180919_1312'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='plan',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]