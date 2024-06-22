# serializers/province_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import Province
    
class ProvinceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Province
        fields = '__all__'
