# inventory/views/provinces_view.py
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from ..models import Province
from ..serializers.province_serializer import ProvinceSerializer
from rest_framework.permissions import IsAuthenticated

class ProvinceViewSet(ReadOnlyModelViewSet):
    serializer_class = ProvinceSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Province.objects.all()
