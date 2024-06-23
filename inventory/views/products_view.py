# inventory/views/products_view.py
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from ..models import Product
from ..serializers.product_serializer import ProductSerializer, ProductSerializerRestrict
from rest_framework.permissions import IsAuthenticated

class ProductViewSet(ReadOnlyModelViewSet):
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Product.objects.all()
        request = self.request.query_params

        # Filtrage par sector_code
        sector_code = request.get('sector_code')
        if sector_code:
            queryset = queryset.filter(sector_code=sector_code)

        # Filtrage par sector_label
        sector_label = request.get('sector_label')
        if sector_label:
            queryset = queryset.filter(sector_label__icontains=sector_label)

        # Filtrage par activity_code
        activity_code = request.get('activity_code')
        if activity_code:
            queryset = queryset.filter(activity_code=activity_code)

        # Filtrage par activity_label
        activity_label = request.get('activity_label')
        if activity_label:
            queryset = queryset.filter(activity_label__icontains=activity_label)

        # Filtrage par product_code
        product_code = request.get('product_code')
        if product_code:
            queryset = queryset.filter(product_code=product_code)

        # Filtrage par product_label
        product_label = request.get('product_label')
        if product_label:
            queryset = queryset.filter(product_label__icontains=product_label)

        return queryset
