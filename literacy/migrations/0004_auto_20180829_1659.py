# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-29 13:59
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('literacy', '0003_auto_20180829_1358'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stkpush_online_payment',
            old_name='tansacrion_description',
            new_name='tansaction_description',
        ),
    ]