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
    path('', include(router.urls)),
]
