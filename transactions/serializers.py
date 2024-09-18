from rest_framework import serializers
from .models import Payments, Collections


class PaymentsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Payments
    fields = ["amount", "account_name", "account_number", "account_issuer", "external_transaction_id"]


class CollectionsSerializer(serializers.ModelSerializer):
  class Meta:
    model = Collections
    fields = ["amount", "transaction_status", "account_name", "account_number", "account_issuer", "callback_url"]