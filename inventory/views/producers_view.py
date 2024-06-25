# inventory/views/producers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
# from ..serializers.producer_serializer import ProducerListSerializer, ProducerDetailSerializer

from django.contrib.auth.models import User
from inventory.models import Producer
from inventory.serializers.producer_serializer import ProducerSerializer
from django.contrib.auth import get_user_model


from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import ProducerForm
import json
from django.shortcuts import redirect

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer
    permission_classes = [IsAuthenticated]


def index(request):
    return render(request, 'inventory/producers/index.html', {})

def producer_list(request):
    producers = Producer.objects.all()
    return render(request, 'inventory/producers/producer_list.html', {'producers': producers})

# def add_producer(request):
#     if request.method == 'POST':
#         form = ProducerForm(request.POST, request.FILES)
#         if form.is_valid():
#             producer = form.save()
#             return HttpResponse(
#                 status=204,
#                 headers={
#                     'HX-Trigger': json.dumps({
#                         'producerListChanged': None,
#                         'showMessage': f'{producer.company_name} ajouté.'
#                     })
#                 }
#             )
#         else:
#             return render(request, 'inventory/producers/producer_form.html', {'form': form})
#     else:
#         form = ProducerForm()
#     return render(request, 'inventory/producers/producer_form.html', {'form': form})

# def edit_producer(request, pk):
#     producer = get_object_or_404(Producer, pk=pk)
#     if request.method == 'POST':
#         form = ProducerForm(request.POST, request.FILES, instance=producer)
#         if form.is_valid():
#             producer = form.save()
#             return HttpResponse(
#                 status=204,
#                 headers={
#                     'HX-Trigger': json.dumps({
#                         'producerListChanged': None,
#                         'showMessage': f'{producer.company_name} mis à jour.'
#                     })
#                 }
#             )
#         else:
#             return render(request, 'inventory/producers/producer_form.html', {'form': form, 'producer': producer})
#     else:
#         form = ProducerForm(instance=producer)
#     return render(request, 'inventory/producers/producer_form.html', {'form': form, 'producer': producer})

def add_producer(request):
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES)
        if form.is_valid():
            producer = form.save()
            return redirect('producer_list')  # Redirige vers producer_list
        else:
            return render(request, 'inventory/producers/producer_form.html', {'form': form})
    else:
        form = ProducerForm()
    return render(request, 'inventory/producers/producer_form.html', {'form': form})

def edit_producer(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    if request.method == 'POST':
        form = ProducerForm(request.POST, request.FILES, instance=producer)
        if form.is_valid():
            producer = form.save()
            return redirect('producer_list')  # Redirige vers producer_list
        else:
            return render(request, 'inventory/producers/producer_form.html', {'form': form, 'producer': producer})
    else:
        form = ProducerForm(instance=producer)
    return render(request, 'inventory/producers/producer_form.html', {'form': form, 'producer': producer})

def remove_producer_confirmation(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    return render(request, 'inventory/producers/producer_delete_confirmation.html', {'producer': producer})

@require_POST
def remove_producer(request, pk):
    producer = get_object_or_404(Producer, pk=pk)
    company_name = producer.company_name  # Pour l'utilisation dans le message de confirmation
    
    producer.delete()
    
    # Redirection vers producer_list avec un message
    return redirect('producer_list')