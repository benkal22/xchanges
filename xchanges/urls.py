from django.contrib import admin
from django.urls import path, include
from inventory.views.base_view import IndexView
# from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path
from inventory.views.registration_view import SignUpView, CustomLoginView, CustomLogoutView, CustomPasswordResetView, profile_view
from inventory.views.registration_view import ResetPassword, RequestPasswordReset

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
    path('inventory/', include('inventory.urls')),
]

