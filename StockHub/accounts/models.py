# accounts/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    # AbstractUser already includes: username, password, first_name, last_name, email, is_staff...
    company = models.CharField(max_length=255, blank=True, null=True)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    
    # Role choices: 'admin' and 'staff' (you can expand)
    ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('staff', 'Staff'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='staff')

    def __str__(self):
        return self.username
