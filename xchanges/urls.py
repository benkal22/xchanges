# xchanges/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

from inventory.views.company_clients_view import CompanyClientViewSet
from inventory.views.personal_clients_view import PersonalClientViewSet
from inventory.views.producers_view import ProducerViewSet
from inventory.views.products_view import ProductViewSet
from inventory.views.provinces_view import ProvinceViewSet
from inventory.views.purchases_view import PurchaseViewSet
from inventory.views.sales_view import SaleViewSet
from inventory.views.suppliers_view import SupplierViewSet

router = DefaultRouter()
router.register(r'producers', ProducerViewSet, basename='producers')
router.register(r'products', ProductViewSet, basename='products')
router.register(r'provinces', ProvinceViewSet, basename='provinces')
router.register(r'suppliers', SupplierViewSet, basename='suppliers')
router.register(r'company_clients', CompanyClientViewSet, basename='company_clients')
router.register(r'personal_clients', PersonalClientViewSet, basename='personal_clients')
router.register(r'purchases', PurchaseViewSet, basename='purchases')
router.register(r'sales', SaleViewSet, basename='sales')

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('inventory.urls')),
    path('api/', include(router.urls)),
    
    path('api-auth/', include('rest_framework.urls')), 
    
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
]