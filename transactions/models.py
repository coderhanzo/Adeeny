from django.db import models
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField
from django.contrib.auth import get_user_model

# Create your models here.

# 2 tables: payments(donations) and collections(WAQF donations)
User = get_user_model()


# this model will replace donations
class Payments(models.Model):
    NETWORK_TYPE_CHOICES = (
        ("MTN", "MTN"),
        ("TELECEL", "Telecel"),
        ("AIRTELTIGO", "AirtelTigo"),
    )
    amount = models.CharField(required=True, max_length=100)
    account_name = models.CharField(required=True, max_length=100)
    account_number = models.CharField(required=True, max_length=100)
    account_issuer = models.CharField(
        required=True, max_length=100, choices=NETWORK_TYPE_CHOICES
    )
    external_transaction_id = models.CharField(required=True, max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_name} {self.account_number} {self.created_at}"


# this model will replace WAQF donations/ projectdonations
class Collections(models.Model):
    NETWORK_TYPE_CHOICES = (
        ("MTN", "MTN"),
        ("TELECEL", "Telecel"),
        ("AIRTELTIGO", "AirtelTigo"),
    )
    PAYMENT_STATUS_CHOICES = [
        ("pending", "Pending"),
        ("completed", "Completed"),
        ("failed", "Failed"),
    ]
    amount = models.CharField(required=True, max_length=100)
    transaction_status = models.CharField(
        max_length=10, choices=PAYMENT_STATUS_CHOICES, default="pending"
    )
    account_name = models.CharField(required=True, max_length=100)
    account_number = models.CharField(required=True, max_length=100)
    account_issuer = models.CharField(required=True, max_length=100, choices=NETWORK_TYPE_CHOICES)
    callback_url = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Collection: {self.amount} - {self.transaction_status} - {self.external_transaction_id}"


