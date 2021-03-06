from django.contrib import admin
from accounts.models import *
from django.contrib.auth.admin import UserAdmin
from django.forms import TextInput, Textarea, CharField
from django import forms
from django.db import models


class UserAdminConfig(UserAdmin):
    model = Account
    search_fields = ("email", "username", "first_name", "last_name")
    list_filter = ("email", "username", "first_name", "last_name", "type", "is_active", "is_staff")

    ordering = ("-dateUpdated",)
    list_display = ("id", "email", "username", "first_name", "last_name", "type", "is_active", "is_staff")
    fieldsets = (
        (None, {"fields": ("email", "username", "first_name", "last_name")}),
        (
            "Permissions",
            {"fields": ("type", "is_staff", "is_active", "is_verified")},
        ),
        (
            "Personal",
            {
                "fields": (
                    "about",
                    "profileImage",
                    "profileCover",
                )
            },
        ),
        (
            "Group Permissions",
            {
                "classes": ("collapse",),
                "fields": (
                    "groups",
                    "user_permissions",
                ),
            },
        ),
    )
    formfield_overrides = {
        models.TextField: {"widget": Textarea(attrs={"rows": 20, "cols": 60})},
    }
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "first_name",
                    "last_name",
                    "username",
                    "email",
                    "password1",
                    "password2",
                    "about",
                    "profileImage",
                    "profileCover",
                    "type",
                    "is_active",
                    "is_staff",
                ),
            },
        ),
    )


admin.site.register(Account, UserAdminConfig)
