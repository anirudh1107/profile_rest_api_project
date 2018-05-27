from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.

class UserProfileManager(BaseUserManager):
    """Helps Django work woth our customer model"""

    def create_user(self,email,name,password=None):
        """Creates a new user profile object"""

        if not email:
            raise ValueError('users must have a email address')

        email=self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self._db)

    def create_superuser(self,email,name,password):
        """Create ad save a new super user with given details"""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a user profile inside our system."""

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    object = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']


    def get_full_name(self):
        """used to get full name """

        return self.name

    def get_short_name(self):
        """used to get short name."""

        return self.name

    def __str__(self):
        """django uses to convert object to string"""

        return self.email
