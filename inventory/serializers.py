# serializers.py of app:inventory of project:xchanges

from rest_framework import serializers
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale

class ProducerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = '__all__'

class CompanyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyClient
        fields = '__all__'

class PersonalClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalClient
        fields = '__all__'

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'
