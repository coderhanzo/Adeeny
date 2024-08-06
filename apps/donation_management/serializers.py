from rest_framework import serializers
from .models import ProjectDonation
from phonenumber_field.serializerfields import PhoneNumberField
from utils.exceptions import validate_phonenumber
from utils.utils import Base64FileField


class MonetaryDoantionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDonation
        fields = ["donations", "phone_numnber", "amount", "payment_type", "donors_name"]


class WaqfDonationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDonation
        fields = [
            "title",
            "description",
            "upload_image",
            "target_amount",
            "imams_name",
            "payment_type",
        ]
