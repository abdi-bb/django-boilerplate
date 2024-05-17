from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.utils.translation import gettext as _
from django.urls import include, path
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.routers import DefaultRouter
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from dj_rest_auth.views import LoginView
from dj_rest_auth.registration.views import RegisterView, SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client

from accounts.models import Profile
from .permissions import (
    IsUserProfileOwner,
)
from .serializers import (
    UserRegisterSerializer,
    UserLoginSerializer,
    UserDetailsSerializer,
    ProfileDetailsSerializer,
)

User = get_user_model()

class UserRegisterationAPIView(RegisterView):
    """
    Register new users using email and password.
    """

    serializer_class = UserRegisterSerializer

    def create(self, request, *args, **kwargs):
        """
        Create a new user.
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        
        response_data = ''

        email = serializer.validated_data.get('email', None)

        if email:
            response_data = {'detail': _('Verification email sent.')}

        return Response(response_data, status=status.HTTP_201_CREATED, headers=headers)

class UserLoginAPIView(LoginView):
    """
    Authenticate existing users using email and password.
    """

    serializer_class = UserLoginSerializer


class GoogleLogin(SocialLoginView):
    """
    Social authentication with Google
    """
    
    adapter_class = GoogleOAuth2Adapter
    callback_url = "call_back_url"
    client_class = OAuth2Client


class ProfileDetailsAPIView(RetrieveUpdateAPIView):
    """
    Get, Update user profile
    """

    queryset = Profile.objects.all()
    serializer_class = ProfileDetailsSerializer
    permission_classes = (IsUserProfileOwner,)

    def get_object(self):
        return self.request.user.profile



class UserDetailsAPIView(RetrieveAPIView):
    """
    Get user details
    """

    queryset = User.objects.all()
    serializer_class = UserDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user

