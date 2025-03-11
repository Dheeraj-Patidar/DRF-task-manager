from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser, Task


class CustomUserAdmin(UserAdmin):
    list_display = ["first_name", "last_name", "email", "is_staff"]
    ordering = ["email"]
    search_fields = ("email",)

    # ✅ Customize the fieldsets to remove 'username'
    fieldsets = (
        (None, {"fields": ("email", "password")}),

        (
            "Permissions",
            {
                "fields": (
                    "is_staff",
                    "is_active",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        ("Personal Data", {"fields": ("first_name", "last_name")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )

    # ✅ Define fields for user creation in the admin panel
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2", "is_staff", "is_active"),
            },
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)


class TaskAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "description",
        "status",
        "assigned_to",
        "created_at",
        "updated_at",
    ]


admin.site.register(Task, TaskAdmin)
