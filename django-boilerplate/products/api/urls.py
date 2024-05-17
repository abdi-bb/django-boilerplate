from rest_framework.routers import DefaultRouter
from .views import ProductViewSet

product_router = DefaultRouter()
product_router.register(r'products', ProductViewSet)