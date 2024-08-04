from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from phonenumbers.data.region_IR import PHONE_METADATA_IR

from src.users.managers import UserManager
from src.utils.models import TimeStampedModel, UuidModel


class User(AbstractUser, UuidModel, TimeStampedModel):
    """User model representing a user in the application."""

    class Gender(models.TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")

    # authentication info
    phone = PhoneNumberField(
        _("Phone number"),
        unique=True,
        region=PHONE_METADATA_IR.id,
        null=True,
        default=None,
    )
    phone_verified = models.BooleanField(_("Is phone number verified"), default=False)

    # personal info
    email = models.EmailField(_("email address"), null=True, unique=True)
    birth_date = models.DateField(_("Birth date"), null=True, blank=True)
    gender = models.CharField(
        choices=Gender.choices,
        default=Gender.MALE,
        max_length=1,
        verbose_name=_("Gender"),
    )

    objects = UserManager()

    REQUIRED_FIELDS = []

    class Meta:
        indexes = [
            models.Index(fields=["username"], name="username_indx"),
            models.Index(fields=["first_name", "last_name"], name="full_name_indx"),
        ]
        ordering = ["-created_at"]
        verbose_name = _("User")
        verbose_name_plural = _("Users")
