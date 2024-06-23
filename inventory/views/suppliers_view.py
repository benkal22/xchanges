# inventory/views/suppliers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Supplier
from ..serializers.supplier_serializer import SupplierSerializer
from rest_framework.permissions import IsAuthenticated

class SupplierViewSet(viewsets.ModelViewSet):
    serializer_class = SupplierSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Supplier.objects.all()

