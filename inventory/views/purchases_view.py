# inventory/views/purchases_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Purchase
from ..serializers.purchase_serializer import PurchaseSerializer
from rest_framework.permissions import IsAuthenticated

class PurchaseViewSet(viewsets.ModelViewSet):
    serializer_class = PurchaseSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Purchase.objects.all()