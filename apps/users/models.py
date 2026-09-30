from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email=models.EmailField(unique=True, blank=False, null=False)
    username = models.CharField(max_length=150)
    fullname = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
