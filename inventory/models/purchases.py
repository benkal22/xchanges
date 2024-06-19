from django.db import models

from inventory.models.producers import Producer
from inventory.models.products import Product
from inventory.models.suppliers import Supplier

#Achat chez le fournisseur
class Purchase(models.Model):
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE, related_name='supplier_purchase')
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_purchase')
    # product = models.ForeignKey(Product, null=True, on_delete=models.CASCADE, related_name='product_purchase')
    product = models.ManyToManyField(Product)
    price = models.fields.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.fields.IntegerField()
    tva = models.fields.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.fields.DateField()
    def __str__(self) -> str:
        return f'{self.quantity}'
