from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError


# Create your models here


def upload_to(instance, filename):
    return "profile/{filename}".format(filename=filename)


class User(AbstractUser):
    class Roles(models.TextChoices):
        ADMIN = "ADMIN", _("Admin")
        IMAM = "IMAM", _("Imam")
        ASSCOCIATE = "ASSOCIATE", _("Associate")
        USER = "USER", _("User")

    username = None
    profile_pic = models.ImageField(
        _("Profile Picture"),
        upload_to=upload_to,
        blank=True,
        null=True,
        default="profile/default.jpg",
    )
    # name = models.CharField(verbose_name=_("Name"), max_length=250, default="n/a")
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    phone_number = PhoneNumberField(
        verbose_name=_("Phone Number"),
        max_length=30,
        blank=True,
        null=True,
        unique=True,
    )
    roles = models.CharField(
        max_length=10,
        choices=Roles.choices,
        default=Roles.USER,
        verbose_name=_("User Roles"),
    )
    is_verified = models.BooleanField(_("Is Verified"), default=False)
    # verification_code = models.CharField(max_length=6, blank=True, null=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
        "phone_number",
    ]

    objects = CustomUserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return (f"{self.first_name} {self.last_name}")

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
