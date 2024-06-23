from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from inventory.forms.registration_form import SignUpForm, CustomAuthenticationForm, CustomPasswordResetForm
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.contrib.sites.shortcuts import get_current_site
from django.template.response import TemplateResponse
from django.views.generic.edit import FormView
from django.urls import reverse_lazy

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from inventory.models.users import CustomUser, PasswordReset
from rest_framework import status
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import os
from inventory.serializers.user_serializer import ResetPasswordRequestSerializer, ResetPasswordSerializer

from django.core.mail import send_mail
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text

User = get_user_model()

class SignUpView(FormView):
    template_name = 'inventory/registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save(commit=False)
        # user.is_active = False  # Optionnel : désactiver le compte jusqu'à confirmation par email, par exemple
        user.save()
        return super().form_valid(form)

class CustomLoginView(LoginView):
    template_name = 'inventory/registration/login.html'
    authentication_form = CustomAuthenticationForm

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')
    
class CustomPasswordResetView(FormView):
    template_name = 'inventory/registration/password_reset.html'
    form_class = PasswordResetForm
    success_url = reverse_lazy('password_reset_done')

    def form_valid(self, form):
        form.save(
            request=self.request,
            use_https=self.request.is_secure(),
            email_template_name='inventory/registration/password_reset_email.html',
            subject_template_name='inventory/registration/password_reset_subject.txt',
            domain_override=get_current_site(self.request).domain,
            html_email_template_name='inventory/registration/password_reset_email.html',
        )
        return super().form_valid(form)
class RequestPasswordReset(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordRequestSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['email']
            user = CustomUser.objects.filter(email__iexact=email).first()

            if user:
                token_generator = PasswordResetTokenGenerator()
                token = token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                reset = PasswordReset(email=email, token=token)
                reset.save()

                reset_url = f"{os.getenv('PASSWORD_RESET_BASE_URL')}/{uid}/{token}/"

                # Envoi de l'email de réinitialisation
                send_mail(
                    'Password Reset Request',
                    f'Click the link to reset your password: {reset_url}',
                    'noreply@yourdomain.com',
                    [email],
                    fail_silently=False,
                )

                return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "User with this email not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ResetPassword(generics.GenericAPIView):
    permission_classes = [AllowAny]
    serializer_class = ResetPasswordSerializer

    def post(self, request, uidb64, token):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                uid = force_text(urlsafe_base64_decode(uidb64))
                user = CustomUser.objects.get(pk=uid)
            except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
                user = None

            if user is not None and PasswordResetTokenGenerator().check_token(user, token):
                new_password = serializer.validated_data['new_password']
                confirm_password = serializer.validated_data['confirm_password']

                if new_password == confirm_password:
                    user.set_password(new_password)
                    user.save()
                    return Response({'success': 'Password has been reset.'}, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Passwords do not match'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'error': 'Invalid token or user ID'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@login_required
def profile_view(request):
    return render(request, 'inventory/registration/profile.html')
