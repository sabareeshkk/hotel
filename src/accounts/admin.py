"""Accounts app admin model."""
from django.contrib import admin

from .models import User
# Register your models here.


class UserAdmin(admin.ModelAdmin):
    """User admin details."""

    pass

admin.site.register(User, UserAdmin)
