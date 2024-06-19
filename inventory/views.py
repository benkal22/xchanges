# inventory/views.py
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework import generics, permissions
from .models import Producer, Product, Province, Supplier, CompanyClient, PersonalClient, Purchase, Sale
from .serializers import ProducerSerializer, ProductSerializer, ProvinceSerializer, SupplierSerializer, CompanyClientSerializer, PersonalClientSerializer, PurchaseSerializer, SaleSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model

class HomeView(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request):
        content = {'message': 'Welcome to the JWT Authentication page using React Js and Django!'}
        return Response(content)

class ProducerViewSet(viewsets.ModelViewSet):
    queryset = Producer.objects.all()
    serializer_class = ProducerSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProvinceViewSet(viewsets.ModelViewSet):
    queryset = Province.objects.all()
    serializer_class = ProvinceSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer

class CompanyClientViewSet(viewsets.ModelViewSet):
    queryset = CompanyClient.objects.all()
    serializer_class = CompanyClientSerializer

class PersonalClientViewSet(viewsets.ModelViewSet):
    queryset = PersonalClient.objects.all()
    serializer_class = PersonalClientSerializer

class PurchaseViewSet(viewsets.ModelViewSet):
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer

class SaleViewSet(viewsets.ModelViewSet):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
