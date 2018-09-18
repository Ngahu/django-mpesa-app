# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User = get_user_model()

from django.db.models.signals import pre_save

from .utils import unique_reference_id_generator



class StkPush_Online_Payment(models.Model):
    user = models.ForeignKey(User,blank=True, null=True)
    business_short_code = models.PositiveIntegerField()
    password = models.CharField(max_length=250)
    timestamp =  models.CharField(max_length=50)
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







class StkPush_Call_Back(models.Model):
    """
    Description:Save the results from mpesa after a successful stk push
    """
    merchant_request_id = models.CharField(max_length=250,blank=True, null=True)
    checkout_request_id = models.CharField(max_length=250,blank=True, null=True)
    result_code = models.CharField(max_length=250,blank=True, null=True)
    result_description = models.CharField(max_length=250,blank=True, null=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.merchant_request_id







class PurchaseRequest(models.Model):
    """
    Description:Save all request initiated by user
    """
    user = models.ForeignKey(User)
    product_id = models.PositiveSmallIntegerField()
    unique_reference_id = models.CharField(max_length=12,blank=True, null=True)
    date_added = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.unique_reference_id




def purchase_request_pre_save_receiver(sender,instance,*args,**kwargs):
    if not instance.unique_reference_id:
        instance.unique_reference_id = unique_reference_id_generator(instance)

    



pre_save.connect(purchase_request_pre_save_receiver,sender=PurchaseRequest)







class PaymentTransactions(models.Model):
    """
    Description:Save the transaction details \n
    """
    user = models.ForeignKey(User,blank=True, null=True)
    timestamp =  models.CharField(max_length=50)
    transaction_type = models.CharField(max_length=100)
    amount = models.CharField(max_length=100)
    