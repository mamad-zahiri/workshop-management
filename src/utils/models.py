from uuid import uuid4

from django.db import models
from django.utils.translation import gettext_lazy as _


class UuidModel(models.Model):
    """An abstract model that uses UUID for ID."""

    id = models.UUIDField(_("ID"), primary_key=True, default=uuid4, editable=False)

    class Meta:
        abstract = True
