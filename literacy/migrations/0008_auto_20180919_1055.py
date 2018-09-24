# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 07:55
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('literacy', '0007_auto_20180918_1634'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentTransactions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.CharField(max_length=50)),
                ('transaction_type', models.CharField(max_length=100)),
                ('amount', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=50)),
                ('account_reference', models.CharField(max_length=12, unique=True)),
                ('transaction_description', models.CharField(max_length=13)),
                ('merchant_request_id', models.CharField(blank=True, max_length=250, null=True)),
                ('checkout_request_id', models.CharField(blank=True, max_length=250, null=True)),
                ('response_code', models.CharField(blank=True, max_length=250, null=True)),
                ('result_description', models.CharField(blank=True, max_length=250, null=True)),
                ('mpesa_receipt_number', models.CharField(max_length=20, unique=True)),
                ('balance', models.IntegerField()),
                ('transaction_date', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('FAILED', 'Failed'), ('PENDING', 'Pending'), ('SUCCESSFUL', 'successful')], max_length=12)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='purchaserequest',
            name='product_id',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
