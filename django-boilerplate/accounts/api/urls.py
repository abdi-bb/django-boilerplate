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
    UserDetailsAPIView,
    UserRegisterationAPIView,
    UserLoginAPIView,
    GoogleLogin,
    ProfileDetailsAPIView,
)

from django.urls import path

from django.urls import include
from dj_rest_auth.registration.views import ConfirmEmailView

urlpatterns = [
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ), # Needs to be defined before the registration path
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('dj_rest_auth.registration.urls'))
]

# Email verification
from dj_rest_auth.registration.views import VerifyEmailView
urlpatterns += [
    path(
        'account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),
]

# Password reset
from dj_rest_auth.views import PasswordResetConfirmView
urlpatterns += [
    path(
        'password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
]

# Profile (Custom added views)
from .views import ProfileDetailsAPIView

urlpatterns += [
    path('profile/', ProfileDetailsAPIView.as_view(), name='profile-detail'),
]

# Social login
from .views import GoogleLogin
from .views import UserRedirectView

urlpatterns += [
    path('google/', GoogleLogin.as_view(), name='google_login'),
    path("~redirect/", view=UserRedirectView.as_view(), name="redirect")
]