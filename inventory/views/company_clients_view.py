# inventory/views/company_clients_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import CompanyClient
from ..serializers.company_client_serializer import CompanyClientSerializer
from rest_framework.permissions import IsAuthenticated

from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.views.generic import ListView
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from inventory.filters import CompanyClientFilter
from inventory.tables import CompanyClientTable

class CompanyClientViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyClientSerializer
    def get_queryset(self):
        return CompanyClient.objects.all()
    permission_classes = [IsAuthenticated]

#View Front

# class CompanyClientsView(LoginRequiredMixin, TemplateView):
#     template_name = 'inventory/client/client_list.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['company_clients'] = CompanyClient.objects.all()
#         return context

class CompanyClientsView(SingleTableMixin, FilterView):
    model = CompanyClient
    table_class = CompanyClientTable
    filterset_class = CompanyClientFilter
    template_name = 'inventory/client/client_list.html'
    paginate_by = 10  # Nombre d'éléments par page
    
# def company_clients_list(request):
#     f = CompanyClientFilter(request.GET, queryset=CompanyClient.objects.all())
#     return render(request, 'inventory/client/client_list.html', {'filter': f})

