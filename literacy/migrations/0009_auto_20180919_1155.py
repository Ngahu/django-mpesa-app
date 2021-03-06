# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-19 08:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0008_auto_20180919_1055'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('period', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='purchaserequest',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='literacy.PaymentPlan'),
        ),
    ]
