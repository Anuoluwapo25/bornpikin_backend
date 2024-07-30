from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    name = models.CharField(max_length=255, blank=True)
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=15, blank=True)
    location = models.CharField(max_length=255, blank=True)

    REQUIRED_FIELDS = ['email', 'phone_number', 'location', 'name']

    def __str__(self):
        return self.email
