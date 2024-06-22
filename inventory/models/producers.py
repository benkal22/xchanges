from django.db import models, transaction
from django.contrib.auth.models import AbstractUser, Group, Permission, AbstractBaseUser, PermissionsMixin
from inventory.models.products import Product
from inventory.models.provinces import Province
# from inventory.models.users import CustomUser

# Producer model défini comme utilisateur de l'application
class Producer(models.Model):
    # user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=True, primary_key=True, related_name='producer_profile')
    company_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    profile_photo = models.ImageField(verbose_name='Photo de profil entreprise', blank=True, null=True)
    address = models.CharField(max_length=255)
    tax_code = models.CharField(max_length=100, blank=True, null=True)
    nrc = models.CharField(max_length=100, blank=True, null=True)
    nat_id = models.CharField(max_length=100, blank=True, null=True)
    phone_number = models.CharField(max_length=20)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='producer_province')
    product = models.ManyToManyField(Product, blank=True, related_name='producers')
    sector_label = models.CharField(blank=True, null=True, max_length=200)
    about = models.CharField(blank=True, null=True, max_length=1000)
    is_actived = models.BooleanField(default=True)
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return self.company_name
    
    # groups = models.ManyToManyField(
    #     Group,
    #     related_name='producers',
    #     blank=True,
    #     help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    #     verbose_name='groups',
    # )

    # user_permissions = models.ManyToManyField(
    #     Permission,
    #     related_name='producer_users',
    #     blank=True,
    #     help_text='Specific permissions for this user.',
    #     verbose_name='user permissions',
    # )
    
    @transaction.atomic
    def disable(self):
        if self.is_actived is False:
            return 
        self.is_actived = False
        self.save()