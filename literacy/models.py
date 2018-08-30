# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()



class StkPush_Online_Payment(models.Model):
    user = models.ForeignKey(User,blank=True, null=True)
    business_short_code = models.PositiveIntegerField()
    password = models.CharField(max_length=250)
    timestamp =  models.DateTimeField()
    transaction_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    party_a = models.CharField(max_length=100)
    party_b = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    callback_url = models.CharField(max_length=100)
    account_reference= models.CharField(max_length=12)
    tansaction_description = models.CharField(max_length=13)
    date_done = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



    def __str__(self):
        return str(self.timestamp)
