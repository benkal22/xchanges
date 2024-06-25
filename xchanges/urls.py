from django.contrib import admin
from django.urls import path, include
from inventory.views.base_view import IndexView
# from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path
from inventory.views.registration_view import SignUpView, CustomLoginView, CustomLogoutView, CustomPasswordResetView, profile_view
from inventory.views.registration_view import ResetPassword, RequestPasswordReset

from inventory.views.company_clients_view import CompanyClientsView
# from inventory.views.personal_clients_view import PersonalClientView
# from inventory.views.producers_view import ProducerView
# from inventory.views.provinces_view import ProvinceView
# from inventory.views.suppliers_view import SupplierView
# from inventory.views.purchases_view import PurchaseView
# from inventory.views.sales_view import SaleView
# from inventory.views.products_view import ProductView

from inventory.views.personal_clients_view import PersonalClientViewSet
from inventory.views.producers_view import ProducerViewSet
from inventory.views.provinces_view import ProvinceViewSet
from inventory.views.suppliers_view import SupplierViewSet
from inventory.views.purchases_view import PurchaseViewSet
from inventory.views.sales_view import SaleViewSet
from inventory.views.products_view import ProductViewSet

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('inventory.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', IndexView.as_view(), name='index'),
    
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('profile/', profile_view, name='profile'),
    
    # Inclure les URLs de réinitialisation de mot de passe de Django
    # path('password_reset/', include('django.contrib.auth.urls')),
    
    #Path personnalisés Front
    path('company-clients/', CompanyClientsView.as_view(), name='company_clients_list'),

    path('personal-clients/', PersonalClientViewSet.as_view({'get': 'list'}), name='personal_clients_list'),
    path('producers/', ProducerViewSet.as_view({'get': 'list'}), name='producers_list'),
    path('products/', ProductViewSet.as_view({'get': 'list'}), name='products_list'),
    path('provinces/', ProvinceViewSet.as_view({'get': 'list'}), name='provinces_list'),
    path('purchases/', PurchaseViewSet.as_view({'get': 'list'}), name='purchases_list'),
    # path('sales/', SaleViewSet.as_viewSet({'get': 'list'}), name='sales_list'),
    path('suppliers/', SupplierViewSet.as_view({'get': 'list'}), name='suppliers_list'),
    
    #Actually Path
    path('inventory/', include('inventory.urls')),
]

# from django.contrib import admin
# from django.urls import path, include
# from inventory.views.base_view import IndexView
# # from django.views.generic import TemplateView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from django.urls import path
# from inventory.views.registration_view import SignUpView, CustomLoginView, CustomLogoutView, CustomPasswordResetView, profile_view
# from inventory.views.registration_view import ResetPassword, RequestPasswordReset

# from inventory.views.company_clients_view import CompanyClientsView
# # from inventory.views.personal_clients_view import PersonalClientView
# # from inventory.views.producers_view import ProducerView
# # from inventory.views.provinces_view import ProvinceView
# # from inventory.views.suppliers_view import SupplierView
# # from inventory.views.purchases_view import PurchaseView
# # from inventory.views.sales_view import SaleView
# # from inventory.views.products_view import ProductView

# from inventory.views.personal_clients_view import PersonalClientViewSet
# from inventory.views.producers_view import ProducerViewSet
# from inventory.views.provinces_view import ProvinceViewSet
# from inventory.views.suppliers_view import SupplierViewSet
# from inventory.views.purchases_view import PurchaseViewSet
# from inventory.views.sales_view import SaleViewSet
# from inventory.views.products_view import ProductViewSet

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('api/', include('inventory.urls')),
#     path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('', IndexView.as_view(), name='index'),
    
#     path('signup/', SignUpView.as_view(), name='signup'),
#     path('login/', CustomLoginView.as_view(), name='login'),
#     path('logout/', CustomLogoutView.as_view(), name='logout'),
#     path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
#     # path('reset_password/<str:token>/', ResetPassword.as_view(), name='password_reset_confirm'),
#     path('profile/', profile_view, name='profile'),
    
#     # Inclure les URLs de réinitialisation de mot de passe de Django
#     path('password_reset/', include('django.contrib.auth.urls')),
#     # path('password_reset/', RequestPasswordReset.as_view(), name='password_reset'),
#     # path('reset_password/<str:token>/', ResetPassword.as_view(), name='reset_password'),
    
#     #Path personnalisés Front
#     path('company-clients/', CompanyClientsView.as_view(), name='company_clients_list'),
#     # path('company-clients/', company_clients_list, name='company_clients_list'),
#     # path('personal-clients/', PersonalClientView.as_view({'get': 'list'}), name='personal_clients_list'),
#     # path('producers/', ProducerView.as_view({'get': 'list'}), name='producers_list'),
#     # path('products/', ProductView.as_view({'get': 'list'}), name='products_list'),
#     # path('provinces/', ProvinceView.as_view({'get': 'list'}), name='provinces_list'),
#     # path('purchases/', PurchaseView.as_view({'get': 'list'}), name='purchases_list'),
#     # path('sales/', SaleView.as_view({'get': 'list'}), name='sales_list'),
#     # path('suppliers/', SupplierView.as_view({'get': 'list'}), name='suppliers_list'),
    
#     path('personal-clients/', PersonalClientViewSet.as_view({'get': 'list'}), name='personal_clients_list'),
#     path('producers/', ProducerViewSet.as_view({'get': 'list'}), name='producers_list'),
#     path('products/', ProductViewSet.as_view({'get': 'list'}), name='products_list'),
#     path('provinces/', ProvinceViewSet.as_view({'get': 'list'}), name='provinces_list'),
#     path('purchases/', PurchaseViewSet.as_view({'get': 'list'}), name='purchases_list'),
#     # path('sales/', SaleViewSet.as_viewSet({'get': 'list'}), name='sales_list'),
#     path('suppliers/', SupplierViewSet.as_view({'get': 'list'}), name='suppliers_list'),
    
    
# ]
