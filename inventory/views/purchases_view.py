# inventory/views/purchases_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import Purchase
from inventory.serializers.purchase_serializer import PurchaseSerializer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import PurchaseForm
from django.shortcuts import redirect

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]

def purchases_list(request):
    purchases = Purchase.objects.all()
    return render(request, 'inventory/purchases/purchases_list.html', {'purchases': purchases})

def add_purchase(request):
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES)
        if form.is_valid():
            purchase = form.save()
            return redirect('purchases_list')  # Redirige vers purchases_list
        else:
            return render(request, 'inventory/purchases/purchase_form.html', {'form': form})
    else:
        form = PurchaseForm()
    return render(request, 'inventory/purchases/purchase_form.html', {'form': form})

def edit_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    if request.method == 'POST':
        form = PurchaseForm(request.POST, request.FILES, instance=purchase)
        if form.is_valid():
            purchase = form.save()
            return redirect('purchases_list')  # Redirige vers purchases_list
        else:
            return render(request, 'inventory/purchases/purchase_form.html', {'form': form, 'purchase': purchase})
    else:
        form = PurchaseForm(instance=purchase)
    return render(request, 'inventory/purchases/purchase_form.html', {'form': form, 'purchase': purchase})

def remove_purchase_confirmation(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    return render(request, 'inventory/purchases/purchase_delete_confirmation.html', {'purchase': purchase})

@require_POST
def remove_purchase(request, pk):
    purchase = get_object_or_404(Purchase, pk=pk)
    company_name = purchase.company_name  # Pour l'utilisation dans le message de confirmation
    
    purchase.delete()
    
    # Redirection vers purchases_list avec un message
    return redirect('purchases_list')