# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-21 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0015_auto_20180921_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='paymenttransactions',
            name='customer_message',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='paymenttransactions',
            name='response_description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='paymenttransactions',
            name='result_code',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]