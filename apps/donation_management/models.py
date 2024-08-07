from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.

# class Donation(models.Model):
#   name = models.CharField(max_length=200, verbose_name=_("Account Name"), blank=True, null=True)
#   phone_numnber = PhoneNumberField(verbose_name=_("Phone Number"), blank=True, null=True)
#   ammount = models.PositiveIntegerField(verbose_name=_("Amount"), blank=True, null=True)
#   created_at = models.DateTimeField(auto_now_add=True)
  
#   def __str__(self):
#     return self.name


class ProjectDonation(models.Model):
    """
    payment type will be a dropdown menu
    """
    class PaymentType(models.TextChoices):
        CASH = "CASH", _("Cash")
        CREDIT_CARD = "CREDIT_CARD", _("Credit Card")
        DEBIT_CARD = "DEBIT_CARD", _("Debit Card")
    title = models.CharField(
        verbose_name=_("WAQF Title"), max_length=50, blank=True, null=True
    )
    donors_name = models.CharField(
        verbose_name=_("Donations"), max_length=50, blank=True, null=True
    )
    phone_numnber = PhoneNumberField(verbose_name=_("Phone Number"), blank=True, null=True)
    description = models.TextField(verbose_name=_("Description"), blank=True, null=True)

    def user_directory_path(instance, filename):
        # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        return "user_{0}/{1}".format("WAQF Upload", filename)

    upload_image = models.FileField(verbose_name=_("Upload Image"), upload_to=user_directory_path, blank=True, null=True)
    imams_name = models.CharField(verbose_name=_("Imam's Name"), max_length=250, blank=True, null=True) # make the name of the imam a foreign key with the imam user/profile
    payment_type = models.CharField(choices=PaymentType.choices, verbose_name=_("Payment Type"), max_length=250, blank=True, null=True) 
    amount = models.PositiveIntegerField(verbose_name=_("Amount"), blank=True, null=True) # this will be the for donations data
    target_amount = models.PositiveIntegerField(verbose_name=_("Target Amount"), blank=True, null=True) # this will be the waqf data
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

def __str__(self):
    return self.title

