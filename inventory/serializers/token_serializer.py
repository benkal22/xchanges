from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    """Customizes JWT default Serializer to add more information about user"""
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['name'] = user.name
        token['email'] = user.email
        token['is_superuser'] = user.is_superuser
        token['is_staff'] = user.is_staff
        token['is_admin'] = user.is_admin
        token['is_producer'] = user.is_producer

        return token