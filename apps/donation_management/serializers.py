from rest_framework import serializers
from .models import ProjectDonation
from phonenumber_field.serializerfields import PhoneNumberField
from utils.exceptions import validate_phonenumber
from utils.utils import Base64FileField


class CreateProjectDonationSerializer(serializers.ModelSerializer):
    image = Base64FileField()

    class Meta:
        model = ProjectDonation
        fields = ["title", "payment_type", "target_amount"]


class DonationSerializer(serializers.ModelSerializer):
    phone_number = PhoneNumberField(region="GH", validators=[validate_phonenumber])

    class Meta:
        model = ProjectDonation
        fields = "__all__"
