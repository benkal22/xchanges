# inventory/filters.py
import django_filters
from inventory.models import CompanyClient

class CompanyClientFilter(django_filters.FilterSet):
    class Meta:
        model = CompanyClient
        fields = {
            'nom': ['icontains'],
            'email': ['exact'],
            # Ajoutez d'autres champs pour le filtrage
        }