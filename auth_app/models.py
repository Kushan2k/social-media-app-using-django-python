from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import CustomUserManager
from .common.models import BaseModel
from django.contrib.auth.models import PermissionsMixin

class CustomUser(BaseModel,AbstractUser,PermissionsMixin):
    bio=models.TextField(blank=False,null=False)
    dob=models.DateField(blank=False,null=False)
    email=models.EmailField(unique=True,blank=False,null=False)
    is_active=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username','first_name','last_name','bio','dob']

    objects=CustomUserManager()


    