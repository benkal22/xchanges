# serializers/product_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductSerializerRestrict(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'sector_label', 'activity_label', 'product_label']
    