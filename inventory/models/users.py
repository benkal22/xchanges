# inventory/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models
from ..managers import CustomUserManager

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)  # Champ email unique
    
    # Définir le champ USERNAME_FIELD à 'username' et REQUIRED_FIELDS à ['email']
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()  # Utilisez le gestionnaire personnalisé

    def __str__(self):
        return self.username
