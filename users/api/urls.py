from django.urls import include, path, re_path
from django.views.generic import TemplateView
from rest_framework.routers import DefaultRouter
from dj_rest_auth.registration.views import ResendEmailVerificationView, VerifyEmailView
from dj_rest_auth.views import (
    LogoutView,
    PasswordChangeView,
    PasswordResetConfirmView,
    PasswordResetView,
)

from .views import (
    UserAPIView,
    UserRegisterationAPIView,
    UserLoginAPIView,
    GoogleLogin,
    ProfileAPIView,
)

# from .views import ProductViewSet

# product_router = DefaultRouter()
# product_router.register(r'products', ProductViewSet)

urlpatterns = [
    path('', UserAPIView.as_view(), name='user-detail'),
    path('register/', UserRegisterationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('login/google/', GoogleLogin.as_view(), name='google-login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileAPIView.as_view(), name='profile-detail'),

    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),

    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path(
        "resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"
    ),
    re_path(
        r"^account-confirm-email/(?P<key>[-:\w]+)/$",
        VerifyEmailView.as_view(),
        name="account_confirm_email",
    ),
    path(
        "account-email-verification-sent/",
        TemplateView.as_view(),
        name="account_email_verification_sent",
    ),
]