# from inventory.serializers.token_serializer import TokenObtainPairSerializer

# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


# class CustomTokenObtainPairView(TokenObtainPairView):
#     # Replace the serializer with your custom
#     serializer_class = TokenObtainPairSerializer

from django.views.generic import TemplateView

class IndexView(TemplateView):
    # template_name = 'index.html'
    template_name = 'inventory/index.html'
    
    

