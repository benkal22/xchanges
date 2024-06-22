# inventory/views/company_clients_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import CompanyClient
from ..serializers.company_client_serializer import CompanyClientSerializer

class CompanyClientViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyClientSerializer
    def get_queryset(self):
        return CompanyClient.objects.all()
