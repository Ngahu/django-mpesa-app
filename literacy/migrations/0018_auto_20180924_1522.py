# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-24 12:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0017_auto_20180924_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paymenttransactions',
            name='amount',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='balance',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='result_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='status',
            field=models.CharField(choices=[('FAILED', 'Failed'), ('PENDING', 'Pending'), ('SUCCESSFUL', 'successful')], default='PENDING', max_length=12),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='transaction_date',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='transaction_description',
            field=models.CharField(blank=True, max_length=13, null=True),
        ),
        migrations.AlterField(
            model_name='paymenttransactions',
            name='transaction_type',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
