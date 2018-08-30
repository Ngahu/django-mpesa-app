from rest_framework import serializers

from .models import StkPush_Online_Payment



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
