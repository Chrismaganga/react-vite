from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CartItemViewSet

router = DefaultRouter()
router.register('products', ProductViewSet)
router.register('cart', CartItemViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
