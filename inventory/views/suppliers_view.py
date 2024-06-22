# inventory/views/suppliers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Supplier
from ..serializers.supplier_serializer import SupplierSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer
    def get_queryset(self):
        return Supplier.objects.all()

