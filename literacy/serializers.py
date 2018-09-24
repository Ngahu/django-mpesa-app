from rest_framework import serializers

from .models import (
    StkPush_Online_Payment,
    StkPush_Call_Back,
    PurchaseRequest,
    PaymentTransactions
    )



class ResponseSaveSerializer(serializers.ModelSerializer):
    """
    Description:Serializer to save the response returned immediately after an stk push
    """
    class Meta:
        model = PaymentTransactions
        fields = [
            'user',
            'merchant_request_id',
            'checkout_request_id',
            'response_code',
            'response_description',
            'customer_message',
            'timestamp',
            'account_reference',
            'amount'
            
        ]

        def create(self,validated_data):
            new_response = PaymentTransactions(
                user=validated_data['user'],
                merchant_request_id=validated_data['merchant_request_id'],
                checkout_request_id = validated_data['checkout_request_id'],
                response_code = validated_data['response_code'],
                response_description = validated_data['response_description'],
                customer_message = validated_data['customer_message'],
                timestamp = validated_data['timestamp'],
                account_reference = validated_data['account_reference'],
                amount = validated_data['amount']
            )

            new_response.save()

            return new_response






class CallbackSaveSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentTransactions
        fields = [
            'merchant_request_id',
            'checkout_request_id',
            'result_code',
            'result_description'
            
        ]


        def create(self,validated_data):
            new_callback_result = PaymentTransactions(
                merchant_request_id=validated_data['merchant_request_id'],
                checkout_request_id = validated_data['checkout_request_id'],
                result_code = validated_data['result_code'],
                result_description = validated_data['result_description']
            )

            new_callback_result.save()


            return new_callback_result










class PurchaseRequestItializeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PurchaseRequest
        fields = [
            'user',
            'product_id',
            'plan'
        ]

        def create(self,validated_data):
            new_purchase_request = PurchaseRequest(
                user = validated_data['user'],
                product_id = validated_data['product_id'],
                plan = validated_data['plan'],
            )
            new_purchase_request.save()

            return new_purchase_request







class StkPush_Online_PaymentCreateSerializer(serializers.ModelSerializer):
    """
    Description:Serializer to serialize the data during the initalizing of an STK
    """
    class Meta:
        model = StkPush_Online_Payment
        fields = [
            "business_short_code",
            "password", 
            "timestamp",   
            "transaction_type", 
            "amount",
            "party_a",
            "party_b",
            "phone_number",
            "callback_url",
            "account_reference",
            "tansaction_description",

        ]

        def create(self,validated_data):
            new_trans = StkPush_Online_Payment(
                business_short_code = validated_data['business_short_code'],
                password = validated_data['password'],
                timestamp = validated_data['timestamp'],
                transaction_type = validated_data['transaction_type'],
                amount = validated_data['amount'],
                party_a = validated_data['party_a'],
                party_b = validated_data['party_b'],
                phone_number = validated_data['phone_number'],
                callback_url = validated_data['callback_url'],
                account_reference  = validated_data['account_reference'],
                tansaction_description = validated_data['tansaction_description']                
            )
            new_trans.save()
            return new_trans





class StkPush_Call_Back_CreateSerializer(serializers.ModelSerializer):
    """
    Description:Serialize the data passed by the callback
    """
    class Meta:
        model = StkPush_Call_Back
        fields = [
            'merchant_request_id',
            'checkout_request_id',
            'result_code',
            'result_description'
        ]


        def create(self,validated_data):
            new_callback = StkPush_Call_Back(
                merchant_request_id=validated_data['merchant_request_id'],
                checkout_request_id = validated_data['checkout_request_id'],
                result_code = validated_data['result_code'],
                result_description = validated_data['result_description']
            )
            new_callback.save()
            
            return new_callback

