# inventory/views/company_clients_view.py
from rest_framework import viewsets
from ..models import CompanyClient
from ..serializers.company_client_serializer import CompanyClientSerializer
from rest_framework.permissions import IsAuthenticated

class CompanyClientViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyClientSerializer
    def get_queryset(self):
        return CompanyClient.objects.all()
    permission_classes = [IsAuthenticated]

# class CompanyClientsView(SingleTableMixin, FilterView):
#     model = CompanyClient
#     table_class = CompanyClientTable
#     filterset_class = CompanyClientFilter
#     template_name = 'inventory/client/client_list.html'
#     paginate_by = 10  # Nombre d'éléments par page

from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import CompanyClient
from inventory.serializers.company_client_serializer import CompanyClientSerializer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import CompanyClientForm
from django.shortcuts import redirect

class CompanyClientViewSet(viewsets.ModelViewSet):
    queryset = CompanyClient.objects.all()
    serializer_class = CompanyClientSerializer
    permission_classes = [IsAuthenticated]

def company_clients_list(request):
    company_clients = CompanyClient.objects.all()
    return render(request, 'inventory/clients/company_clients/company_clients_list.html', {'company_clients': company_clients})

def add_company_client(request):
    if request.method == 'POST':
        form = CompanyClientForm(request.POST, request.FILES)
        if form.is_valid():
            company_client = form.save()
            return redirect('company_clients_list')  # Redirige vers company_clients_list
        else:
            return render(request, 'inventory/clients/company_clients/company_client_form.html', {'form': form})
    else:
        form = CompanyClientForm()
    return render(request, 'inventory/clients/company_clients/company_client_form.html', {'form': form})

def edit_company_client(request, pk):
    company_client = get_object_or_404(CompanyClient, pk=pk)
    if request.method == 'POST':
        form = CompanyClientForm(request.POST, request.FILES, instance=company_client)
        if form.is_valid():
            company_client = form.save()
            return redirect('company_clients_list')  # Redirige vers company_clients_list
        else:
            return render(request, 'inventory/clients/company_clients/company_client_form.html', {'form': form, 'company_client': company_client})
    else:
        form = CompanyClientForm(instance=company_client)
    return render(request, 'inventory/clients/company_clients/company_client_form.html', {'form': form, 'company_client': company_client})

def remove_company_client_confirmation(request, pk):
    company_client = get_object_or_404(CompanyClient, pk=pk)
    return render(request, 'inventory/clients/company_clients/company_client_delete_confirmation.html', {'company_client': company_client})

@require_POST
def remove_company_client(request, pk):
    company_client = get_object_or_404(CompanyClient, pk=pk)
    company_name = company_client.company_name  # Pour l'utilisation dans le message de confirmation
    
    company_client.delete()
    
    # Redirection vers company_clients_list avec un message
    return redirect('company_clients_list')
