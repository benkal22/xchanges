# serializers/personal_client_serializer.py of app:inventory of project:xchanges

from rest_framework import serializers
from ..models import PersonalClient

class PersonalClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalClient
        fields = '__all__'
