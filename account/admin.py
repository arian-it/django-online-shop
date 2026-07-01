from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from account.models import User, Otp



class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.

    list_display = ["full_name", "email", "phone", 'is_superuser', 'is_active']
    list_filter = ["is_superuser", "is_active"]

    fieldsets = [
        (None, {"fields": ["email", "password"]}),
        ("Personal info", {"fields": ["full_name"]}),
        ("Permissions", {"fields": ["is_staff", "is_superuser", "is_active", "groups", "user_permissions"]}),
    ]
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["full_name", "email", "password1", "password2", 'is_staff', 'phone', 'is_superuser', 'is_active', 'groups', 'user_permissions'],
            },
        ),
    ]
    search_fields = ["full_name", 'email', 'phone']
    ordering = ["full_name"]
    filter_horizontal = ["groups", "user_permissions"]


admin.site.register(User, UserAdmin)
admin.site.register(Otp)
