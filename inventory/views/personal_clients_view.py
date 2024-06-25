# inventory/views/personal_clients_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import PersonalClient
from inventory.serializers.personal_client_serializer import PersonalClientSerializer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import PersonalClientForm
from django.shortcuts import redirect

class PersonalClientViewSet(viewsets.ModelViewSet):
    queryset = PersonalClient.objects.all()
    serializer_class = PersonalClientSerializer
    permission_classes = [IsAuthenticated]

def personal_clients_list(request):
    personal_clients = PersonalClient.objects.all()
    return render(request, 'inventory/clients/personal_clients/personal_clients_list.html', {'personal_clients': personal_clients})

def add_personal_client(request):
    if request.method == 'POST':
        form = PersonalClientForm(request.POST, request.FILES)
        if form.is_valid():
            personal_client = form.save()
            return redirect('personal_clients_list')  # Redirige vers personal_clients_list
        else:
            return render(request, 'inventory/clients/personal_clients/personal_client_form.html', {'form': form})
    else:
        form = PersonalClientForm()
    return render(request, 'inventory/clients/personal_clients/personal_client_form.html', {'form': form})

def edit_personal_client(request, pk):
    personal_client = get_object_or_404(PersonalClient, pk=pk)
    if request.method == 'POST':
        form = PersonalClientForm(request.POST, request.FILES, instance=personal_client)
        if form.is_valid():
            personal_client = form.save()
            return redirect('personal_clients_list')  # Redirige vers personal_clients_list
        else:
            return render(request, 'inventory/clients/personal_clients/personal_client_form.html', {'form': form, 'personal_client': personal_client})
    else:
        form = PersonalClientForm(instance=personal_client)
    return render(request, 'inventory/clients/personal_clients/personal_client_form.html', {'form': form, 'personal_client': personal_client})

def remove_personal_client_confirmation(request, pk):
    personal_client = get_object_or_404(PersonalClient, pk=pk)
    return render(request, 'inventory/clients/personal_clients/personal_client_delete_confirmation.html', {'personal_client': personal_client})

@require_POST
def remove_personal_client(request, pk):
    personal_client = get_object_or_404(PersonalClient, pk=pk)
    company_name = personal_client.personal_client_name  # Pour l'utilisation dans le message de confirmation
    
    personal_client.delete()
    
    # Redirection vers personal_clients_list avec un message
    return redirect('personal_clients_list')