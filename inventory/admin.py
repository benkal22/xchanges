from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale
from django.contrib.auth import get_user_model

User = get_user_model()

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Producer)
# admin.site.register(Producer, UserAdmin)
admin.site.register(Product)
admin.site.register(Province)
admin.site.register(Supplier)
admin.site.register(CompanyClient)
admin.site.register(PersonalClient)
admin.site.register(Purchase)
admin.site.register(Sale)
