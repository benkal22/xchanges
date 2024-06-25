from django.db import models
from inventory.models.users import CustomUser
from inventory.models.products import Product, ProductProd
from inventory.models.producers import Producer
from inventory.models.clients import Client, CompanyClient, PersonalClient
from inventory.models.provinces import Province
from inventory.models.purchases import Purchase, PurchaseOrder, PurchaseOrderItem
from inventory.models.sales import Sale, SalesOrder, SalesOrderItem
from inventory.models.suppliers import Supplier

