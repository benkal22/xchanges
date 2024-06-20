# inventory/views/producers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from ..models import Producer
from ..serializers import ProducerSerializer

class ProducerViewSet(viewsets.ModelViewSet):
    serializer_class = ProducerSerializer
    def get_queryset(self):
        return Producer.objects.all()