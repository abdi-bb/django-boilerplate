from django.urls import include, path, re_path

from .views import ProfileDetailsAPIView

urlpatterns = [
    path(r'', include('djoser.urls')),
    path(r'users/', include('djoser.urls.authtoken')), # Token based authentication
    path(r'users/', include('djoser.urls.jwt')), # JWT based authentication
]

urlpatterns += [
    path('users/profile/', ProfileDetailsAPIView.as_view(), name='profile-detail'),
]