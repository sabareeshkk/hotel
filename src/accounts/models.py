"""Extending Baseusermodel to our custome model."""
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _

from .managers import UserManager

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    """user model for auth."""

    email = models.EmailField(max_length=254, unique=True, db_index=True)
    user_name = models.CharField(_('user name'), max_length=30)
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into admin site'))
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether user should be treated as active.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_name']

    def get_short_name(self):
        """Return the short name for the user."""
        return self.user_name

    def get_full_name(self):
        """Full name."""
        return self.user_name
