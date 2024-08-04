from django.contrib.auth.models import UserManager as BaseUserManager


class UserManager(BaseUserManager):
    """Manager for the `User` model."""

    @classmethod
    def normalize_email(cls, email):
        """Default email normalizer but return None if email is None or empty."""
        if email is None or email == "":
            return None

        return cls.normalize_email(email)
