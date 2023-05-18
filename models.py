from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.core.validators import RegexValidator, EmailValidator

class User(models.Model):
    mobile = models.CharField(max_length=10, blank=False, null=False, unique=True)
    email = models.EmailField(max_length=50, blank=True, null=False)
    password = models.CharField(max_length=50, blank=False, null=False)
    otp = models.CharField(max_length=6, blank=True, null=True)

