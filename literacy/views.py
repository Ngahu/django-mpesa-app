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

from .serializers import StkPush_Online_PaymentCreateSerializer



def to_bs(timestamp):
    short_code = "601490"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"

    the_date = str(timestamp)
    result = base64.b64encode(short_code+passkey+the_date)
    return str(result)



class PaymentAPIView(APIView):
    """
    """

    def post(self,request,*args,**kwargs):
        current_time = datetime.datetime.now()
        print(current_time)


        business_short_code = request.data['business_short_code']
        transaction_type = request.data['transaction_type'] 
        amount = request.data['amount']
        party_a = request.data['party_a']
        party_b = request.data['party_b']
        phone_number = request.data['phone_number']
        callback_url = request.data['callback_url']
        account_reference = request.data['account_reference']
        tansaction_description = request.data['tansacrion_description']
        # timestamp = request.data['timestamp']
        # password = request.data['password']


        timestamp = current_time
        password = to_bs(current_time)

        print(password)

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
            "timestamp":timestamp,
            "password":password
        }

        serializer_class = StkPush_Online_PaymentCreateSerializer(data=data)

        if serializer_class.is_valid():
            new_trans = serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)








class CallBackURL(APIView):

    def post(self,request,*args,**kwargs):
        request_data = request.data
        print(request_data)


        message = {
        "ResultCode": 0,
        "ResultDesc": "The service was accepted successfully",
        "ThirdPartyTransID": "1234567890"
        }
        
        return Response(message,status=status.HTTP_200_OK)
