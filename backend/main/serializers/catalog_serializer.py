
from main.models import Catalog
from rest_framework import serializers

class CatalogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catalog
        fields = ['id', 'name']