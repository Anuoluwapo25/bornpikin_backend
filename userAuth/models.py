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
    

class BookUser(models.Model):
    name = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    services = models.CharField(max_length=255, blank=True)
    dentist = models.CharField(max_length=255, blank=True)
    date = models.DateField(max_length=15, blank=True)
    time = models.TimeField(max_length=15, blank=True)
    is_completed = models.BooleanField(default=False)


    def __str__(self):
        return self.dentist
