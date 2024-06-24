
# inventory/views/sales_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Sale
from ..serializers.sale_serializer import SaleSerializer
from rest_framework.permissions import IsAuthenticated

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Sale.objects.all()
