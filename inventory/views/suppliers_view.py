# inventory/views/suppliers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from inventory.models import Supplier
from inventory.serializers.supplier_serializer import SupplierSerializer

from django.shortcuts import render, get_object_or_404
from django.views.decorators.http import require_POST
from inventory.forms.all_forms import SupplierForm
from django.shortcuts import redirect

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]

def suppliers_list(request):
    suppliers = Supplier.objects.all()
    return render(request, 'inventory/suppliers/suppliers_list.html', {'suppliers': suppliers})

def add_supplier(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES)
        if form.is_valid():
            supplier = form.save()
            return redirect('suppliers_list')  # Redirige vers suppliers_list
        else:
            return render(request, 'inventory/suppliers/supplier_form.html', {'form': form})
    else:
        form = SupplierForm()
    return render(request, 'inventory/suppliers/supplier_form.html', {'form': form})

def edit_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    if request.method == 'POST':
        form = SupplierForm(request.POST, request.FILES, instance=supplier)
        if form.is_valid():
            supplier = form.save()
            return redirect('suppliers_list')  # Redirige vers suppliers_list
        else:
            return render(request, 'inventory/suppliers/supplier_form.html', {'form': form, 'supplier': supplier})
    else:
        form = SupplierForm(instance=supplier)
    return render(request, 'inventory/suppliers/supplier_form.html', {'form': form, 'supplier': supplier})

def remove_supplier_confirmation(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    return render(request, 'inventory/suppliers/supplier_delete_confirmation.html', {'supplier': supplier})

@require_POST
def remove_supplier(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    company_name = supplier.company_name  # Pour l'utilisation dans le message de confirmation
    
    supplier.delete()
    
    # Redirection vers suppliers_list avec un message
    return redirect('suppliers_list')