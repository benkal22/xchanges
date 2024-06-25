from django.db import models
from inventory.models.products import Product, ProductProd
from inventory.models.producers import Producer
from inventory.models.provinces import Province
from inventory.models.producers import Producer

class Client(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    province = models.CharField(max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='client_province')
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name

#CompanyClient
class CompanyClient(models.Model):
    product = models.ManyToManyField(Product)
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_company_client')
    company_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100, null=True)
    address = models.CharField(max_length=255, null=True)
    tax_code = models.CharField(max_length=100, null=True)
    nrc = models.CharField(max_length=100, null=True)
    nat_id = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='company_client_province')

    class Meta:
        verbose_name = 'Client Entreprise'
        verbose_name_plural = 'Clients Entreprise'
    
    def __unicode__(self):
        return self.company_name
    
    def __str__(self):
        return f'{self.company_name}'

#PersonalClient
class PersonalClient(models.Model):
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_personal_client')
    personal_client_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='personal_client_province')

    class Meta:
        verbose_name = 'Client Personnel'
        verbose_name_plural = 'Clients Personnels'
    
    def __unicode__(self):
        return self.personal_client_name
    
    def __str__(self):
        return f'{self.personal_client_name}'