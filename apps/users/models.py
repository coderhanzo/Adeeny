from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError

# Create your models here.


class User(AbstractUser):
    USER_ROLES = [
        ("ADMIN", "Admin"),
        ("IMAM", "Imam"),
        ("ASSOCIATE", "Associate"),
        ("USER", "User"),
    ]

    username = None
    # is_staff = None
    first_name = models.CharField(verbose_name=_("First Name"), max_length=250, default="n/a")
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=250, default="n/a")
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
        choices=USER_ROLES,
        default="USER",
        verbose_name=_("User Roles"),
    )
    is_verified = models.BooleanField(_("Is Verified"), default=True)
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
        return str(self.email) if self.email else ""

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"
