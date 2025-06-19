from rest_framework import serializers
from .models import Sale
from catalog.serializers import ProductSerializer

class SaleSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Sale
        fields = ['id', 'title', 'description', 'discount_percent', 'products', 'start_date', 'end_date'] 