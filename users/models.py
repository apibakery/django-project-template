from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.timezone import now


class UserManager(BaseUserManager):
    @classmethod
    def normalize_email(cls, email):
        """Normalize entire email to lowercase so we're case-insensitive"""
        return email.lower()

    def get_by_natural_key(self, email):
        """Ignore case for purposes of determining uniqueness"""
        return self.get(email__iexact=email)

    def create_user(self, email, password=None):
        user = self.create(email=email)
        if password:
            user.set_password(password)
            user.save()
        return user

    def create_superuser(self, email, password):
        user = self.create(email=email, is_superuser=True, is_staff=True)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """
    Model used for authenticating users
    """

    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"

    date_joined = models.DateTimeField(
        default=now,
        verbose_name="Joined on",
        help_text="Date and time when the user was created",
    )
    email = models.EmailField(
        max_length=255,
        unique=True,
        verbose_name="Email",
        help_text="User's email address (must be unique)",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name="Active",
        help_text="Whether this user should be treated as active",
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Staff",
        help_text="Whether this user has access to the admin site",
    )
    name = models.CharField(
        max_length=255,
        verbose_name="Name",
        help_text="User's full name",
    )

    objects = UserManager()

    def __str__(self):
        return str(self.name)

    def clean(self):
        super().clean()
        self.email = User.objects.normalize_email(self.email)
