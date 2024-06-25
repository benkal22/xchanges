from django.db import models
from inventory.models.products import Product, ProductProd
from django.utils import timezone

class InventoryTransaction(models.Model):
    TRANSACTION_TYPE_CHOICES = [
        ('IN', 'Incoming'),
        ('OUT', 'Outgoing')
    ]

    product_prod = models.ForeignKey(ProductProd, on_delete=models.CASCADE, related_name="product_prod_inventory")
    transaction_type = models.CharField(max_length=3, choices=TRANSACTION_TYPE_CHOICES)
    quantity = models.PositiveIntegerField()
    transaction_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} of {self.product_prod.product}"
