# inventory/filters.py
import django_filters
from inventory.models import CompanyClient, Supplier

class CompanyClientFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyClient
        fields = {
            'company_name': ['icontains'],
            'email': ['exact'],
            # Ajoutez d'autres champs pour le filtrage
        }

class SupplierFilter(django_filters.FilterSet):
    class Meta:
        model = Supplier
        fields = {
            'company_name': ['icontains'],
            'manager_name': ['icontains'],
            'address': ['icontains'],
            'email': ['icontains'],
            'phone_number': ['icontains'],
            'country': ['icontains'],
            'province': ['exact'],
        }
