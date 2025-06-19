from django.shortcuts import render
from rest_framework import generics, permissions
from .models import DeliveryInfo
from .serializers import DeliveryInfoSerializer

# Create your views here.

class DeliveryInfoDetailView(generics.RetrieveAPIView):
    serializer_class = DeliveryInfoSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Только доставка заказов пользователя
        return DeliveryInfo.objects.filter(order__user=self.request.user)
