from django.db import models

from inventory.models.producers import Producer
from inventory.models.clients import Client
from inventory.models.products import Product, ProductProd
from inventory.models.clients import Client, CompanyClient, PersonalClient
from django.utils import timezone

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
    
    class Meta:
        verbose_name = 'Vente'
        verbose_name_plural = 'Ventes'
    
    def __unicode__(self):
        return self.quantity

class SalesOrder(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='sales_order_producer')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='sales_order_client')
    order_date = models.DateTimeField(default=timezone.now)
    shipped_date = models.DateTimeField(blank=True, null=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return f"SO-{self.id} for {self.client.name}"

class SalesOrderItem(models.Model):
    sales_order = models.ForeignKey(SalesOrder, related_name='items_sale', on_delete=models.CASCADE)
    product_prod = models.ForeignKey(ProductProd, on_delete=models.CASCADE, related_name='sales_product_prod')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product_prod.product}"