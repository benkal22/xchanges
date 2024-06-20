# inventory/views/sales_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Sale
from ..serializers import SaleSerializer

class SaleViewSet(viewsets.ModelViewSet):
    serializer_class = SaleSerializer
    def get_queryset(self):
        return Sale.objects.all()
