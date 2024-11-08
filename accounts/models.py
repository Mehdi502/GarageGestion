
# Create your models here.
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    FUNCTION_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'Utilisateur'),
    ]
    fonction = models.CharField(max_length=10, choices=FUNCTION_CHOICES, default='user')

    def __str__(self):
        return f"{self.username} ({self.fonction})"
