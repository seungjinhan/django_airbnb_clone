from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "User Profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                ),
            },
        ),
    )
    # 어드민 리스트에 보여질 항목
    # list_display = ("username", "email", "gender", "language", "superhost")
    # list_filter = (
    #     "language",
    #     "currency",
    #     "superhost",
    # )
