# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re

from django.shortcuts import render

from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.reverse import reverse
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth import get_user_model
User = get_user_model()
####

from rest_framework.permissions import IsAuthenticated

from datetime import date
import datetime
import base64
import json
import requests

from .models import StkPush_Online_Payment,PaymentTransactions

from .serializers import (
    StkPush_Online_PaymentCreateSerializer,
    StkPush_Call_Back_CreateSerializer,
    PurchaseRequestItializeSerializer,

    ResponseSaveSerializer,
    CallbackSaveSerializer
    )



from requests.auth import HTTPBasicAuth


def generate_auth_token():
    """
    Description:generate the access token required by mpesa for authentication.\n
    """
    consumer_key = "1gWEBFicQT4daQ11WlyPAD494j3MLe8L"
    consumer_secret = "LA7ADyBEbfqDvqEu"
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    response = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))

    # format the response so as to get the token only
    formated_response = json.loads(response.text)
    token = formated_response['access_token']
    
    return token









class RootAPIView(APIView):
    """
    Description:Return  a list of all the endpoints that are going to be used\n
    """

    def get(self,request,format=None):
        return Response({
            "payment-pay":reverse("literacy:storystory_stk_pay", request=request, format=format),
            "call-back":reverse("literacy:call_back", request=request, format=format),
            "initialize-payment":reverse("literacy:initialize_payment", request=request, format=format),
        })






def to_bs(timestamp):
    """
    Description:Generate the password for encrypting the request by base64 encoding BusinessShortcode, Passkey and Timestamp.
    """
    short_code = "174379"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    the_date = str(timestamp)
    result = base64.b64encode(short_code+passkey+the_date)
    return str(result)




class InitializePaymentAPIView(APIView):
    """
    Description:Endpoint to initialize payment \n
    {
    "plan": 2000,
    "product_id": "4"
    }

    {
            "BusinessShortCode": "174379",
            "Password":"MTc0Mzc5YmZiMjc5ZjlhYTliZGJjZjE1OGU5N2RkNzFhNDY3Y2QyZTBjODkzMDU5YjEwZjc4ZTZiNzJhZGExZWQyYzkxOTIwMTgwOTI0MTE1NjE5",
            "Timestamp":"20180924115619",
            "TransactionType": "CustomerPayBillOnline",
            "Amount":"1000",
            "PartyA": "254725743069",
            "PartyB": "174379",
            "PhoneNumber": "254725743069",
            "CallBackURL": "http://23a0390e.ngrok.io/lit/call-back/",
            "AccountReference":"exam",
            "TransactionDesc": "buy exam"
            }
    """
    permission_classes = (IsAuthenticated,)
    
    def post(self,request,*args,**kwargs):
        plan = request.data['plan']
        product_id = request.data['product_id']

        print(generate_auth_token())


        user = request.user.id


        
        data = {
            "plan":plan,
            "product_id":product_id,
            "user":user
        }

        serializer_class = PurchaseRequestItializeSerializer(data=data)


        if serializer_class.is_valid():
            purchase=serializer_class.save()
            # print(purchase.plan)
            # print(purchase.unique_reference_id)


            # initialize the stk push here
            current_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')#this is to format the date

            # timestamp = datetime.datetime.now()
            # timestamp = current_time  #for api call
            password = to_bs(current_time) #for api call
            
            print(password)
            # print(current_time)


            # access_token = "BZbvR78t4fauO5DRkNqXZZuR5Gt4"
            access_token = generate_auth_token()
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = { "Authorization": "Bearer %s" % access_token }
            request = {
            "BusinessShortCode": "174379",
            "Password": password,
            "Timestamp": current_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": purchase.plan,
            "PartyA": "254725743069",
            "PartyB": "174379",
            "PhoneNumber": "254725706302",
            "CallBackURL": "http://0035c6bb.ngrok.io/lit/stk-call-back/",
            "AccountReference": purchase.unique_reference_id,
            "TransactionDesc": "buy exam"
            }
            response = requests.post(api_url, json = request, headers=headers)

            print (response.text)

            # format the response to json
            the_response = json.loads(response.text)


            # # save the response from the mpesa response
            data = {
                "amount":purchase.plan,
                "user":user,
                "checkout_request_id":the_response['CheckoutRequestID'],
                "merchant_request_id":the_response['MerchantRequestID'],
                "response_code":the_response['ResponseCode'],
                "response_description":the_response['ResponseDescription'],
                "customer_message": the_response['CustomerMessage'],
                "timestamp":current_time,
                "account_reference":purchase.unique_reference_id
            }
            stk_response_save_serializer = ResponseSaveSerializer(data=data)

            if stk_response_save_serializer.is_valid():
                new_stk_response = stk_response_save_serializer.save()
                return Response(stk_response_save_serializer.data,status=status.HTTP_201_CREATED)
            
            return Response(stk_response_save_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            


            # print(current_time)


            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer_class.errors,status=status.HTTP_400_BAD_REQUEST)






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
    permission_classes = (IsAuthenticated,)

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
        # print(request.data['Body']['stkCallback'])

        # print(request.data['Body']['stkCallback']['CallbackMetadata']['Item'])
        res = request.data

         

        the_result_code = request.data['Body']['stkCallback']['ResultCode']

        if the_result_code == 0 :
            print("Success request")
            print(res['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']) 
        
        else:
            print("Not a successful request")



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









class STKPushCallBackAPIView(APIView):
    """
    Description:This is the endpoint where safaricom are going to send the callback after a transaction\n
    Expected Responses are either success or error 
    """
    def post(self,request,*args,**kwargs):
        
        # first check that the request is not empty
        if request.data:
            print(request.data)

            # get the result code
            the_result_code = request.data['Body']['stkCallback']['ResultCode']

            if the_result_code == 0:
                # this means its successful save the response here
                print("Success request")
                print(request.data['Body']['stkCallback']['CallbackMetadata']['Item'][1]['Value']) 
            
            else:
                #this means the payment was not success so save the error still 
                print("This is not a successful request")


                merchant_request_id = request.data['Body']['stkCallback']['MerchantRequestID']
                checkout_request_id = request.data['Body']['stkCallback']['CheckoutRequestID']
                result_code = request.data['Body']['stkCallback']['ResultCode']
                result_description = request.data['Body']['stkCallback']['ResultDesc']
                
                # first do a query and get to see if the merchant_request_id and  checkout_request_id do exist
                try:
                    the_transaction = PaymentTransactions.objects.get(merchant_request_id=merchant_request_id,checkout_request_id=checkout_request_id)
                    print(the_transaction)

                    # update the transaction with the result code and result_description
                    the_transaction.result_code = result_code
                    the_transaction.result_description = result_description
                    the_transaction.status = "FAILED"
                    the_transaction.save()



                
                except PaymentTransactions.DoesNotExist:
                    print("multiple objects or doesnt exist")
                    pass


                
        
        else:
            pass
            # print("the request is not valid")
        
        message = {
            "ResultCode": 0,
            "ResultDesc": "The service was accepted successfully",
            "ThirdPartyTransID": "1234567890"
            }
        
        return Response(message,status=status.HTTP_200_OK)
