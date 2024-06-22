# inventory/views/producers_view.py
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from ..serializers.producer_serializer import ProducerListSerializer, ProducerDetailSerializer

from django.contrib.auth.models import User
from inventory.models import Producer
from inventory.serializers.user_serializer import UserSerializer
from inventory.serializers.producer_serializer import ProducerSerializer
from inventory.permissions import IsAdminUser, IsProducerUser
from django.contrib.auth import get_user_model

# User = get_user_model()

# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [IsAuthenticated, IsAdminUser]

# class ProducerViewSet(viewsets.ModelViewSet):
#     queryset = Producer.objects.all()
#     serializer_class = ProducerSerializer
#     permission_classes = [IsAuthenticated, IsProducerUser]

        
# class MultipleSerializerMixin:
#     detail_serializer_class = None
    
#     def get_serializer_class(self):
#         if self.action == 'retrieve' and self.detail_serializer_class is not None:
#             return self.detail_serializer_class
#         return super().get_serializer_class()
    
# class ProducerViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):
#     serializer_class = ProducerListSerializer
    
#     detail_serializer_class = ProducerDetailSerializer
    
#     def get_queryset(self):
#         return Producer.objects.filter(is_active=True)
    
#     def get_serializer_class(self):
#         # Si l'action demandée est retrieve nous retournons le serializer de détail
#         if self.action == 'retrieve':
#             return self.detail_serializer_class
#         return super().get_serializer_class()
    
#     @action(detail=True, methods=['post'])
#     def disable(self, request, pk):
#         self.get_object().disable()
#         return Response()

# class ProducerAdminViewSet(MultipleSerializerMixin, viewsets.ModelViewSet):
#     serializer_class = ProducerListSerializer
    
#     detail_serializer_class = ProducerDetailSerializer
    
#     def get_queryset(self):
#         return Producer.objects.all()
    
#     def get_serializer_class(self):
#         # Si l'action demandée est retrieve nous retournons le serializer de détail
#         if self.action == 'retrieve':
#             return self.detail_serializer_class
#         return super().get_serializer_class()
    
#     @action(detail=True, methods=['post'])
#     def disable(self, request, pk):
#         self.get_object().disable()
#         return Response()
    
#     permission_classes = [IsAuthenticated]
