"""User manager for auth user model."""
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    """manager for creating user and super user."""

    def create_user(self, email, user_name=None, password=None):
        """User creating api."""
        if not email:
            raise ValueError('Users must have an email address')

        # self._check_unique_email(email)

        user = self.model(
            email=self.normalize_email(email),
            user_name=user_name)

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, user_name):
        """Creating superuser."""
        user = self.create_user(
            email=email,
            password=password,
            user_name=user_name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

    def _check_unique_email(self, email):
        try:
            self.get_queryset().get(email=email)
            raise ValueError("This email is already registered")
        except self.model.DoesNotExist:
            return True
