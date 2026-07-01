from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .managers import UserManager

class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=80, blank=True, null=True)
    email = models.EmailField(verbose_name="email address", max_length=255, unique=True, blank=True, null=True)
    phone = models.CharField(max_length=25, unique=True, verbose_name="phone number", blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.phone


class Otp(models.Model):
    phone = models.CharField(max_length=11, unique=True, verbose_name="phone number")
    random_code = models.SmallIntegerField(verbose_name="random code")
    token = models.CharField(max_length=200, unique=True, verbose_name="token", blank=True, null=True)
    expriy_date = models.DateField(verbose_name="expriy date", auto_now_add=True)

    def __str__(self):
        return self.phone
