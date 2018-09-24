# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from .models import (
    StkPush_Online_Payment,
    StkPush_Call_Back,
    PurchaseRequest,
    PaymentTransactions,
    PaymentPlan
    )

class StkPush_Online_PaymentAdmin(admin.ModelAdmin):
    list_display = (
        'business_short_code',
        'phone_number',
        'amount'
    )



admin.site.register(StkPush_Online_Payment,StkPush_Online_PaymentAdmin)





class StkPush_Call_BackAdmin(admin.ModelAdmin):
    list_display = (
        'merchant_request_id',
        'result_code',
        'date_added'
    )


admin.site.register(StkPush_Call_Back,StkPush_Call_BackAdmin)






class PurchaseRequestAdmin(admin.ModelAdmin):
    list_display = (
        'unique_reference_id',
        'product_id',
        'date_added'
    )


admin.site.register(PurchaseRequest,PurchaseRequestAdmin)






class PaymentTransactionsAdmin(admin.ModelAdmin):
    list_display = (
        'merchant_request_id',
        'checkout_request_id',
        # 'phone_number',
        # 'mpesa_receipt_number',
        'status',
        'date_added'
    )


admin.site.register(PaymentTransactions,PaymentTransactionsAdmin)




class PaymentPlanAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'period',
        'price'
    )


admin.site.register(PaymentPlan,PaymentPlanAdmin)