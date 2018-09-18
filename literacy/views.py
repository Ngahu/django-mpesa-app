# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
####


from datetime import date
import datetime
import base64

from .models import StkPush_Online_Payment

from .serializers import (
    StkPush_Online_PaymentCreateSerializer,
    StkPush_Call_Back_CreateSerializer
    )




class RootAPIView(APIView):
    """
    Description:Return  a list of all the endpoints that are going to be used\n
    """

    def get(self,request,format=None):
        return Response({
            "payment-pay":reverse("literacy:storystory_stk_pay", request=request, format=format),
            "call-back":reverse("literacy:call_back", request=request, format=format),
        })










def to_bs(timestamp):
    short_code = "174379"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    the_date = str(timestamp)
    result = base64.b64encode(short_code+passkey+the_date)
    return str(result)



class PaymentAPIView(APIView):
    """
    Description:Endpoint to be used for stk push\n
    Sample Request:\n
    {
      "business_short_code": "174379",
      "transaction_type": "CustomerPayBillOnline",
      "amount": "1200",
      "party_a": "254708374149",
      "party_b": "174379",
      "phone_number": "254708374149",
      "callback_url": "http://7658af3f.ngrok.io/lit/call-back/",
      "account_reference": "Elimu1234",
      "tansaction_description": "bought"
    }\n
    """

    def post(self,request,*args,**kwargs):
        business_short_code = request.data['business_short_code']
        transaction_type = request.data['transaction_type'] 
        amount = request.data['amount']
        party_a = request.data['party_a']
        party_b = request.data['party_b']
        phone_number = request.data['phone_number']
        callback_url = request.data['callback_url']
        account_reference = request.data['account_reference']
        tansaction_description = request.data['tansaction_description']
        # timestamp = request.data['timestamp']
        # password = request.data['password']

        current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')#this is to format the date


        timestamp = datetime.datetime.now()
        # timestamp = current_time  #for api call
        password = to_bs(current_time) #for api call

        print(password)
        print(current_time)

        data = {
            "business_short_code":business_short_code,
            "transaction_type":transaction_type,
            "amount":amount,
            "party_a":party_a,
            "party_b":party_b,
            "phone_number":phone_number,
            "callback_url":callback_url,
            "account_reference":account_reference,
            "tansaction_description":tansaction_description,
            "timestamp":current_time,
            "password":password
        }

        serializer_class = StkPush_Online_PaymentCreateSerializer(data=data)

        if serializer_class.is_valid():
            new_trans = serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)








class CallBackURL(APIView):

    def post(self,request,*args,**kwargs):
        print(request.data)

        merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
        checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
        result_code = request.data['Body']['stkCallback']['ResultCode']
        result_description = request.data['Body']['stkCallback']['ResultDesc']


        # request_data = request.data
        # # print(request_data)
        # print(request.data['Body']['stkCallback']['CheckoutRequestID'])


        data = {
            "merchant_request_id":merchant_request_id,
            "checkout_request_id":checkout_request_id,
            "result_code":result_code,
            "result_description":result_description
        }

        serializer_class = StkPush_Call_Back_CreateSerializer(data=data)
        
        if serializer_class.is_valid():
            new_callback = serializer_class.save()

            message = {
                "ResultCode": 0,
                "ResultDesc": "The service was accepted successfully",
                "ThirdPartyTransID": "1234567890"
            }
            return Response(message,status=status.HTTP_200_OK)
        
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)