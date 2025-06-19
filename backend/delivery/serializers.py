from rest_framework import serializers
from .models import DeliveryInfo

class DeliveryInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryInfo
        fields = ['id', 'order', 'address', 'delivery_date', 'status'] 