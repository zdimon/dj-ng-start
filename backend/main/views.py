from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.response import Response

from .serializers.catalog_serializer import CatalogSerializer
from .serializers.product_serializer import ProductSerializer
from .models import Catalog, Product

class CatalogViewSet(viewsets.ModelViewSet):
    serializer_class = CatalogSerializer
    queryset = Catalog.objects.all()


class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
