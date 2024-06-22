# serializers/company_client_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import CompanyClient

class CompanyClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyClient
        fields = '__all__'
