# inventory/views/provinces_view.py
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import viewsets
from ..models import Province
from ..serializers.province_serializer import ProvinceSerializer

class ProvinceViewSet(ReadOnlyModelViewSet):
    serializer_class = ProvinceSerializer
    def get_queryset(self):
        return Province.objects.all()
