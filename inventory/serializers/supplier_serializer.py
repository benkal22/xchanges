# serializers/supplier_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'
