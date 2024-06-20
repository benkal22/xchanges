from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from inventory.models.products import Product
from inventory.models.provinces import Province

#Producer model défini comme utilisateur de l'application
class Producer(AbstractUser):
    company_name = models.fields.CharField(max_length=100)
    manager_name = models.fields.CharField(max_length=100)
    profile_photo = models.ImageField(verbose_name='Photo de profil entreprise', blank=True, null=True)
    address = models.fields.CharField(max_length=255)
    tax_code = models.fields.CharField(max_length=100, blank=True, null=True)
    nrc = models.fields.CharField(max_length=100, blank=True, null=True)
    nat_id = models.fields.CharField(max_length=100, blank=True, null=True)
    phone_number = models.fields.CharField(max_length=20)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='producer_province')
    product = models.ManyToManyField(Product, blank=True) 
    sector_label =  models.fields.CharField(blank=True, null=True, max_length=200)
    about =  models.fields.CharField(blank=True, null=True, max_length=1000)
    is_active = models.BooleanField(blank=True, default=True)
    is_approved = models.BooleanField(blank=True, default=False)

    def __str__(self) -> str:
        return f'{self.company_name}'
    
    # Champs nécessaires pour éviter les conflits
    groups = models.ManyToManyField(
        Group,
        related_name='producer_set',  # Changez le related_name pour éviter les conflits
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='producer_permissions_set',  # Changez le related_name pour éviter les conflits
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )