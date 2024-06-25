# inventory/views/suppliers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Supplier
from ..serializers.supplier_serializer import SupplierSerializer
from rest_framework.permissions import IsAuthenticated

from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
    
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from inventory.forms.all_forms import SupplierForm
from inventory.tables import SupplierTable
from inventory.filters import SupplierFilter
import django_tables2 as tables
import django_filters

from django.http import JsonResponse
from django.http import HttpResponse 

#API
class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Supplier.objects.all()

#Mon FrontEnd
class SupplierDetailView(DetailView):
    model = Supplier
    template_name = 'inventory/suppliers/detail.html'
    
class SupplierListView(tables.SingleTableView, FilterView):
    model = Supplier
    table_class = SupplierTable
    filterset_class = SupplierFilter
    template_name = 'inventory/suppliers/list.html'    
    paginate_by = 10

    def get_queryset(self):
        # Return your filtered queryset here if needed
        return super().get_queryset()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SupplierForm()  # Ajoutez le formulaire ici
        return context
    
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from inventory.models import Supplier
from inventory.forms.all_forms import SupplierForm

class SupplierCreateView(CreateView):
    model = Supplier
    form_class = SupplierForm
    template_name = 'inventory/suppliers/supplier_form.html'

    def form_valid(self, form):
        form.instance.producer = self.request.user.producer
        supplier = form.save()
        if self.request.htmx:
            return JsonResponse({
                'success': True,
                'message': 'Supplier created successfully!',
                'supplier_id': supplier.id,
                'supplier_name': supplier.company_name,
            })
        else:
            return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.htmx:
            return JsonResponse({
                'success': False,
                'errors': form.errors,
            })
        else:
            return super().form_invalid(form)

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = '__all__'
    template_name = 'inventory/suppliers/form.html'
    success_url = reverse_lazy('supplier_list')

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('supplier_list')