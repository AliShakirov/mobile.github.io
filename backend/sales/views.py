from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Sale
from .serializers import SaleSerializer

# Create your views here.

class SaleListView(generics.ListAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.AllowAny]

class SaleDetailView(generics.RetrieveAPIView):
    queryset = Sale.objects.all()
    serializer_class = SaleSerializer
    permission_classes = [permissions.AllowAny]
