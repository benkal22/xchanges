from django.urls import path, include
from rest_framework.routers import DefaultRouter
from inventory.views.company_clients_view import CompanyClientViewSet
from inventory.views.personal_clients_view import PersonalClientViewSet
from inventory.views.producers_view import ProducerViewSet
from inventory.views.products_view import ProductViewSet
from inventory.views.provinces_view import ProvinceViewSet
from inventory.views.purchases_view import PurchaseViewSet
from inventory.views.sales_view import SaleViewSet
from inventory.views.suppliers_view import SupplierViewSet

from inventory.views.suppliers_view import (
    SupplierListView, SupplierDetailView, SupplierCreateView, SupplierUpdateView, SupplierDeleteView
)
from inventory.views.producers_view import (
    producer_list, add_producer, edit_producer, remove_producer, remove_producer_confirmation
)
router = DefaultRouter()
router.register(r'provinces', ProvinceViewSet, basename='provinces')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'producers', ProducerViewSet, basename='producers')
router.register(r'company-clients', CompanyClientViewSet, basename='company_clients')
router.register(r'personal-clients', PersonalClientViewSet, basename='personal_clients')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'sales', SaleViewSet, basename='sales')

urlpatterns = [
    # path('', include(router.urls)),
    
    path('suppliers/', SupplierListView.as_view(), name='suppliers_list'),
    path('suppliers/<int:pk>/', SupplierDetailView.as_view(), name='supplier_detail'),
    path('suppliers/create/', SupplierCreateView.as_view(), name='supplier_create'),
    path('suppliers/update/<int:pk>/', SupplierUpdateView.as_view(), name='supplier_update'),
    path('suppliers/delete/<int:pk>/', SupplierDeleteView.as_view(), name='supplier_delete'),
    
    path('producers', producer_list, name='producer_list'),
    path('producers/add', add_producer, name='add_producer'),
    path('producers/<int:pk>/edit', edit_producer, name='edit_producer'),
    path('producers/<int:pk>/remove_confirmation', remove_producer_confirmation, name='remove_producer_confirmation'),
    path('producers/<int:pk>/remove', remove_producer, name='remove_producer'),
]

