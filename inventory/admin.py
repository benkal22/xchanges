from django.contrib import admin

# Register your models here.

from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale

admin.site.register(Producer)
admin.site.register(Product)
admin.site.register(Province)
admin.site.register(Supplier)
admin.site.register(CompanyClient)
admin.site.register(PersonalClient)
admin.site.register(Purchase)
admin.site.register(Sale)
