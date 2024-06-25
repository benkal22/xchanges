# inventory/views/sales_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import Sale
from inventory.serializers.sale_serializer import SaleSerializer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import SaleForm
from django.shortcuts import redirect

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]

def sales_list(request):
    sales = Sale.objects.all()
    return render(request, 'inventory/sales/sales_list.html', {'sales': sales})

def add_sale(request):
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES)
        if form.is_valid():
            sale = form.save()
            return redirect('sales_list')  # Redirige vers sales_list
        else:
            return render(request, 'inventory/sales/sale_form.html', {'form': form})
    else:
        form = SaleForm()
    return render(request, 'inventory/sales/sale_form.html', {'form': form})

def edit_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    if request.method == 'POST':
        form = SaleForm(request.POST, request.FILES, instance=sale)
        if form.is_valid():
            sale = form.save()
            return redirect('sales_list')  # Redirige vers sales_list
        else:
            return render(request, 'inventory/sales/sale_form.html', {'form': form, 'sale': sale})
    else:
        form = SaleForm(instance=sale)
    return render(request, 'inventory/sales/sale_form.html', {'form': form, 'sale': sale})

def remove_sale_confirmation(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    return render(request, 'inventory/sales/sale_delete_confirmation.html', {'sale': sale})

@require_POST
def remove_sale(request, pk):
    sale = get_object_or_404(Sale, pk=pk)
    company_name = sale.company_name  # Pour l'utilisation dans le message de confirmation
    
    sale.delete()
    
    # Redirection vers sales_list avec un message
    return redirect('sales_list')