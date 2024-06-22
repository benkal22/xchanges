# serializers/purchase_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import Purchase

class PurchaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchase
        fields = '__all__'
