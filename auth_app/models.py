from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    bio=models.TextField(blank=False,null=False)
    dob=models.DateField(blank=False,null=False)
    