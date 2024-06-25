from django.db import models
from inventory.models.products import Product

class ProductProd(models.Model):
    product = models.ManyToManyField(Product, blank=True, related_name='product_product_prod')
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock_quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.product