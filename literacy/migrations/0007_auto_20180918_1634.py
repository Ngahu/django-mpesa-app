# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-18 13:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0006_purchaserequest'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaserequest',
            name='unique_reference_id',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]