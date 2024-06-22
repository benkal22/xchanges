# serializers/sale_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import Sale

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
