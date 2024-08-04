from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from src.users.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Model admin for `User` model."""

    add_fieldsets = (
        (
            _("Create new user"),
            {
                "classes": ("wide",),
                "fields": (
                    "username",
                    "password1",
                    "password2",
                    "is_staff",
                ),
            },
        ),
    )
    fieldsets = [
        (
            _("Authentication info"),
            {
                "fields": [
                    "id",
                    "email",
                    "password",
                ],
            },
        ),
        (
            _("Personal info"),
            {
                "fields": [
                    "first_name",
                    "last_name",
                    "birth_date",
                    "gender",
                ],
            },
        ),
        (
            _("Permissions"),
            {
                "fields": [
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ],
            },
        ),
        (
            _("Important dates"),
            {
                "fields": [
                    "last_login",
                    "created_at",
                ],
            },
        ),
    ]
    list_display = [
        "username",
        "phone",
        "first_name",
        "last_name",
    ]
    readonly_fields = [
        "id",
        "last_login",
        "modified_at",
        "created_at",
    ]
    list_filter = [
        "is_staff",
        "is_superuser",
        "is_active",
        "gender",
    ]
    search_fields = [
        "first_name",
        "last_name",
        "email",
        "gender",
    ]
    ordering = [
        "username",
    ]
