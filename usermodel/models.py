# models.py in your custom user app

from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from django.conf import settings


class ProductOrService(models.Model):
    # Other fields of your model

    # Define a ForeignKey field referencing the custom user model
    auctioneer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class CustomUserManager(BaseUserManager):
    """
    Custom user manager where email is the unique identifiers
    for authentication instead of usernames.
    """

    def create_user(self, email, password, **extra_fields):
        """
        Create and return a regular user with an email and password.
        """
        if not email:
            raise ValueError(_('The Email field must be set'))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and return a superuser with an email and password.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))

        return self.create_user(email, password, **extra_fields)


class CustomUser(AbstractUser):
    """
    Custom user model with additional fields.
    """
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(_('email address'), unique=True)
    age = models.PositiveIntegerField(blank=True, null=True)
    phone = models.CharField(max_length=11)
    profile_pic = models.ImageField(upload_to='avatar/', blank=True, null=True)

    # Add your custom fields here
    # Example:
    # age = models.PositiveIntegerField(_('age'), null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
