# inventory/views/personal_clients_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import PersonalClient
from ..serializers.personal_client_serializer import PersonalClientSerializer

class PersonalClientViewSet(viewsets.ModelViewSet):
    serializer_class = PersonalClientSerializer
    def get_queryset(self):
        return PersonalClient.objects.all()
