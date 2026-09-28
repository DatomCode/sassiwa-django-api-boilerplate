from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField()
    username = models.CharField()
    fullname = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELDS = 'email'
    REQUIRED_FIELDS = ['email', 'username']

    def __str__(self):
        return self.email
