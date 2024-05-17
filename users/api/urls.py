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

# urlpatterns = [
    # path('password/reset/confirm/<str:uidb64>/<str:token>/', PasswordResetConfirmView.as_view(), name='password-reset-confirm'),

#     path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    
#     re_path(
#         r"^account-confirm-email/(?P<key>[-:\w]+)/$",
#         VerifyEmailView.as_view(),
#         name="account_confirm_email",
#     ),
    
# ]


from django.urls import path

from django.urls import include
from dj_rest_auth.registration.views import ConfirmEmailView, VerifyEmailView
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path(
        'registration/account-confirm-email/<str:key>/',
        ConfirmEmailView.as_view(),
    ), # Needs to be defined before the registration path
    
    path('registration/', UserRegisterationAPIView.as_view(), name='user-register'),
    path('login/', UserLoginAPIView.as_view(), name='user-login'),
    path('google/', GoogleLogin.as_view(), name='google-login'),
    path('profile/', ProfileAPIView.as_view(), name='profile-detail'),
    path('user/', UserAPIView.as_view(), name='user-detail'),
    path('logout/', LogoutView.as_view(), name='logout'),


    # Password
    path('password/reset/', PasswordResetView.as_view(), name='password-reset'),
    path('password/reset/confirm/', PasswordResetConfirmView.as_view(), name='rest_password_reset_confirm'),
    path(
        'password/reset/confirm/<slug:uidb64>/<slug:token>/',
        PasswordResetConfirmView.as_view(), name='password_reset_confirm'
    ),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),

    # Email verification
    path(
        'account-confirm-email/',
        VerifyEmailView.as_view(),
        name='account_email_verification_sent'
    ),

    path('registration/verify-email/', VerifyEmailView.as_view(), name='rest_verify_email'),

    path(
        "registration/resend-email/", ResendEmailVerificationView.as_view(), name="rest_resend_email"
    ),

    re_path(
        r'^account-confirm-email/(?P<key>[-:\w]+)/$', TemplateView.as_view(),
        name='account_confirm_email',
    ),

    path(
        "account-email-verification-sent/",
        TemplateView.as_view(),
        name="account_email_verification_sent",
    ),
    
    # path('', include('dj_rest_auth.urls')),
    # path('registration/', include('dj_rest_auth.registration.urls'))
]

from dj_rest_auth.app_settings import api_settings
if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]
