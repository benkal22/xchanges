# serializers.py of app:inventory of project:xchanges

from rest_framework import serializers
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
        
class ProducerSerializer(serializers.ModelSerializer):
    # product = ProductSerializer(many=True)
    product = serializers.SerializerMethodField()
    class Meta:
        model = Producer
        fields = ['id', 'company_name', 'manager_name', 
                  'product', 'profile_photo', 'address',
                  'tax_code', 'nrc', 'nat_id', 'phone_number', 'province','about']
    
    #Restriction de product
    def get_product(self, instance):
        queryset = instance.product.filter(sector_code='J')
        serializer = ProductSerializer(queryset, many=True)
        return serializer.data    
        
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
