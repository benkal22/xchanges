#inventory/urls

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from inventory.views import (
    ProducerViewSet, ProductViewSet, ProvinceViewSet, SupplierViewSet, 
    CompanyClientViewSet, PersonalClientViewSet, PurchaseViewSet, SaleViewSet,
    HomeView
)

router = routers.DefaultRouter()

router.register(r'producers', ProducerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'company_clients', CompanyClientViewSet)
router.register(r'personal_clients', PersonalClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [ 
   path('home/', HomeView.as_view(), name='home'),                
]