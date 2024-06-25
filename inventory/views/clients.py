# inventory/views/company_clients_view.py
from rest_framework import viewsets
from ..models import CompanyClient, PersonalClient
from ..serializers.company_client_serializer import CompanyClientSerializer
from ..serializers.personal_client_serializer import PersonalClientSerializer
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render


def client_list(request):
    company_clients = CompanyClient.objects.all()
    personal_clients = PersonalClient.objects.all()
    
    return render(request, 'inventory/company_clients/client_list.html', {'company_clients': company_clients, 'personal_clients':personal_clients})
