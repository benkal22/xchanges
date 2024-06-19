# xchanges/urls.py
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework_simplejwt import views as jwt_views

from inventory.views import (
    ProducerViewSet, ProductViewSet, ProvinceViewSet, SupplierViewSet,
    CompanyClientViewSet, PersonalClientViewSet, PurchaseViewSet, SaleViewSet,
)

router = DefaultRouter()
router.register(r'producers', ProducerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'provinces', ProvinceViewSet)
router.register(r'suppliers', SupplierViewSet)
router.register(r'company_clients', CompanyClientViewSet)
router.register(r'personal_clients', PersonalClientViewSet)
router.register(r'purchases', PurchaseViewSet)
router.register(r'sales', SaleViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name ='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name ='token_refresh'),
    path('', include('inventory.urls')),
]
