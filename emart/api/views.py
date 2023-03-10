from rest_framework import viewsets
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class CartItemViewSet(viewsets.ModelViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    def get_queryset(self):
        queryset = CartItem.objects.filter(user=self.request.user)
        return queryset
