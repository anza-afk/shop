from rest_framework import generics
from rest_framework.permissions import AllowAny

from products.models import Product, Category
from products.api.serializers import (
    ProductSerializer,
    CategorySerializer,
)


class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [AllowAny]


class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]
