from django.urls import path, include
from rest_framework.routers import DefaultRouter
from products.api.urls import product_router

router = DefaultRouter()
# can be more extentions like product_router, customer_router, etc.
router.registry.extend(product_router.registry)

urlpatterns = [
    path('', include(router.urls)),
]