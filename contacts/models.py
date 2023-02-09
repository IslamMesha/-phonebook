from django.contrib.auth.models import AbstractUser, User
from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    address = models.CharField(max_length=100, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, unique=True, blank=False)
    email = models.EmailField(max_length=254, unique=True, blank=True)

    def __str__(self):
        return self.name
