from django.db import models

from inventory.models.producers import Producer
from inventory.models.products import Product
from inventory.models.company_clients import CompanyClient
from inventory.models.personal_clients import PersonalClient

#Vente au client
class Sale(models.Model):
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_sale')
    company_id = models.ForeignKey(CompanyClient, on_delete=models.CASCADE, related_name='company_client_sale', null=True)
    personal_client_id = models.ForeignKey(PersonalClient, on_delete=models.CASCADE, related_name='personal_client_sale', null=True)
    product = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    tva = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()
    
    def __str__(self):
        return f'{self.quantity}'
