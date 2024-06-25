from django.db import models

from inventory.models.producers import Producer
from inventory.models.products import Product, ProductProd
from inventory.models.suppliers import Supplier

from django.utils import timezone

#Achat chez le fournisseur
class Purchase(models.Model):
    supplier = models.ForeignKey('Supplier', null=True, on_delete=models.CASCADE, related_name='supplier_purchase')
    producer = models.ForeignKey(Producer, null=True, on_delete=models.CASCADE, related_name='producer_purchase')
    product = models.ManyToManyField(Product)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    tva = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    date = models.DateField()
    
    def __str__(self):
        return f'{self.quantity}'

    class Meta:
        verbose_name = 'Achat'
        verbose_name_plural = 'Achats'
    
    def __unicode__(self):
        return self.quantity

class PurchaseOrder(models.Model):
    producer = models.ForeignKey(Producer, on_delete=models.CASCADE, related_name='producer_purchase_order')
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE, related_name='supplier_purchase_order')
    order_date = models.DateTimeField(default=timezone.now)
    expected_delivery_date = models.DateTimeField()
    received = models.BooleanField(default=False)

    def __str__(self):
        return f"PO-{self.id} from {self.supplier.company_name}"

class PurchaseOrderItem(models.Model):
    purchase_order = models.ForeignKey(PurchaseOrder, related_name='items_purchases', on_delete=models.CASCADE)
    product_prod = models.ForeignKey(ProductProd, on_delete=models.CASCADE, related_name='product_prod_purchases')
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantity} of {self.product_prod.product}"