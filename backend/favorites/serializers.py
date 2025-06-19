from rest_framework import serializers
from .models import Favorite
from catalog.serializers import ProductSerializer

class FavoriteSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    product_id = serializers.PrimaryKeyRelatedField(queryset=Favorite._meta.get_field('product').related_model.objects.all(), source='product', write_only=True)

    class Meta:
        model = Favorite
        fields = ['id', 'product', 'product_id', 'added_at'] 