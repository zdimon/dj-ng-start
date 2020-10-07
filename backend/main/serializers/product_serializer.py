
from main.models import Product
from rest_framework import serializers
from .catalog_serializer import CatalogSerializer

class ProductSerializer(serializers.ModelSerializer):
    catalog = CatalogSerializer()
    class Meta:
        model = Product
        fields = ['id', 'name', 'catalog']