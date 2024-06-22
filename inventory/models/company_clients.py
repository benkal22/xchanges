from django.db import models
from inventory.models.products import Product
from inventory.models.producers import Producer
from inventory.models.provinces import Province

#CompanyClient
class CompanyClient(models.Model):
    product = models.ManyToManyField(Product)
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_company_client')
    company_name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    tax_code = models.CharField(max_length=100, null=True)
    nrc = models.CharField(max_length=100, null=True)
    nat_id = models.CharField(max_length=100, null=True)
    email = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=100)
    province = models.ForeignKey(Province, null=True, on_delete=models.CASCADE, related_name='company_client_province')

    def __str__(self):
        return f'{self.company_name}'
