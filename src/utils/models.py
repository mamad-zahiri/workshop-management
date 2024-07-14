from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class UuidModel(models.Model):
    """An abstract model that uses UUID for ID."""

    id = models.UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True


class TimeStampedModel(models.Model):
    """An abstract model that contains timestamp information.

    Since timestamp fields (created_at, updated_at) are common among almost all
    models, this will help with reducing duplicate code.
    """

    created_at = models.DateTimeField(_("Created at"), auto_now_add=True)
    modified_at = models.DateTimeField(_("Modified at"), auto_now=True)

    class Meta:
        abstract = True
"""  """