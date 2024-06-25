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

from inventory.views.producers_view import (
    producers_list, add_producer, edit_producer, remove_producer, remove_producer_confirmation
)
from inventory.views.sales_view import (
    sales_list, add_sale, edit_sale, remove_sale, remove_sale_confirmation
)
from inventory.views.purchases_view import (
    purchases_list, add_purchase, edit_purchase, remove_purchase, remove_purchase_confirmation
)
from inventory.views.personal_clients_view import (
    personal_clients_list, add_personal_client, edit_personal_client, remove_personal_client, remove_personal_client_confirmation
)
from inventory.views.company_clients_view import (
    company_clients_list, add_company_client, edit_company_client, remove_company_client, remove_company_client_confirmation
)
from inventory.views.suppliers_view import (
    suppliers_list, add_supplier, edit_supplier, remove_supplier, remove_supplier_confirmation
)
from inventory.views.clients import client_list

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
    
    #producers
    path('producers', producers_list, name='producers_list'),
    path('producers/add', add_producer, name='add_producer'),
    path('producers/<int:pk>/edit', edit_producer, name='edit_producer'),
    path('producers/<int:pk>/remove_confirmation', remove_producer_confirmation, name='remove_producer_confirmation'),
    path('producers/<int:pk>/remove', remove_producer, name='remove_producer'),
    
    #suppliers
    path('suppliers', suppliers_list, name='suppliers_list'),
    path('suppliers/add', add_supplier, name='add_supplier'),
    path('suppliers/<int:pk>/edit', edit_supplier, name='edit_supplier'),
    path('suppliers/<int:pk>/remove_confirmation', remove_supplier_confirmation, name='remove_supplier_confirmation'),
    path('suppliers/<int:pk>/remove', remove_supplier, name='remove_supplier'),
    
    #company_clients
    path('clients', client_list, name='client_list'),
    path('clients/company_clients', company_clients_list, name='company_clients_list'),
    path('clients/company_clients/add', add_company_client, name='add_company_client'),
    path('clients/company_clients/<int:pk>/edit', edit_company_client, name='edit_company_client'),
    path('clients/company_clients/<int:pk>/remove_confirmation', remove_company_client_confirmation, name='remove_company_client_confirmation'),
    path('clients/company_clients/<int:pk>/remove', remove_company_client, name='remove_company_client'),
    
    #personaleclient
    path('clients/personal_clients', personal_clients_list, name='personal_clients_list'),
    path('clients/personal_clients/add', add_personal_client, name='add_personal_client'),
    path('clients/personal_clients/<int:pk>/edit', edit_personal_client, name='edit_personal_client'),
    path('clients/personal_clients/<int:pk>/remove_confirmation', remove_personal_client_confirmation, name='remove_personal_client_confirmation'),
    path('clients/personal_clients/<int:pk>/remove', remove_personal_client, name='remove_personal_client'),
    
    #purchases
    path('purchases', purchases_list, name='purchases_list'),
    path('purchases/add', add_purchase, name='add_purchase'),
    path('purchases/<int:pk>/edit', edit_purchase, name='edit_purchase'),
    path('purchases/<int:pk>/remove_confirmation', remove_purchase_confirmation, name='remove_purchase_confirmation'),
    path('purchases/<int:pk>/remove', remove_purchase, name='remove_purchase'),
    
    #sale
    path('sales', sales_list, name='sales_list'),
    path('sales/add', add_sale, name='add_sale'),
    path('sales/<int:pk>/edit', edit_sale, name='edit_sale'),
    path('sales/<int:pk>/remove_confirmation', remove_sale_confirmation, name='remove_sale_confirmation'),
    path('sales/<int:pk>/remove', remove_sale, name='remove_sale'),
    
    #dashboard
    
    
    #products
    
    #provinces
]

