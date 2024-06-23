# serializers/producer_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import Producer
from .product_serializer import ProductSerializerRestrict, ProductSerializer
from .user_serializer import CustomUserSerializer
    
class ProducerSerializer(serializers.ModelSerializer):
    user = CustomUserSerializer()

    class Meta:
        model = Producer
        fields = '__all__'

    # def create(self, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = User.objects.create(**user_data, is_producer=True)
    #     producer = Producer.objects.create(user=user, **validated_data)
    #     return producer

    # def update(self, instance, validated_data):
    #     user_data = validated_data.pop('user')
    #     user = instance.user

    #     instance.company_name = validated_data.get('company_name', instance.company_name)
    #     instance.manager_name = validated_data.get('manager_name', instance.manager_name)
    #     instance.profile_photo = validated_data.get('profile_photo', instance.profile_photo)
    #     instance.address = validated_data.get('address', instance.address)
    #     instance.tax_code = validated_data.get('tax_code', instance.tax_code)
    #     instance.nrc = validated_data.get('nrc', instance.nrc)
    #     instance.nat_id = validated_data.get('nat_id', instance.nat_id)
    #     instance.phone_number = validated_data.get('phone_number', instance.phone_number)
    #     instance.province = validated_data.get('province', instance.province)
    #     instance.sector_label = validated_data.get('sector_label', instance.sector_label)
    #     instance.about = validated_data.get('about', instance.about)
    #     instance.is_actived = validated_data.get('is_actived', instance.is_actived)
    #     instance.is_approved = validated_data.get('is_approved', instance.is_approved)
    #     instance.save()

    #     user.username = user_data.get('username', user.username)
    #     user.email = user_data.get('email', user.email)
    #     user.save()

    #     return instance
 
class ProducerListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producer
        fields = ['id','company_name']
        
    def validate_company_name(self, value):
        # Nous vérifions que la catégorie existe
        if Producer.objects.filter(company_name=value).exists():
        # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Producer already exists')
        return value
    
    def validate_username(self, value):
        # Nous vérifions que la catégorie existe
        if Producer.objects.filter(username=value).exists():
        # En cas d'erreur, DRF nous met à disposition l'exception ValidationError
            raise serializers.ValidationError('Username Producer already exists')
        return value

class ProducerDetailSerializer(serializers.ModelSerializer):
    product = ProductSerializerRestrict(many=True)
    # product = serializers.SerializerMethodField()
    class Meta:
        model = Producer
        fields = ['id', 'company_name', 'manager_name', 
                  'product', 'profile_photo', 'address',
                  'tax_code', 'nrc', 'nat_id', 'phone_number', 'province',
                  'about', 'is_actived', 'is_approved']
        
    #Restriction de product
    # def get_product(self, instance):
    #     queryset = instance.product.filter(sector_code='J')
    #     serializer = ProductSerializer(queryset, many=True)
    #     return serializer.data   

