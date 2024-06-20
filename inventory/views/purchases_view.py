# inventory/views/purchases_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Purchase
from ..serializers import PurchaseSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    def get_queryset(self):
        return Purchase.objects.all()