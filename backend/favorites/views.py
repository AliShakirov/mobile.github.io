from django.shortcuts import render
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from .models import Favorite
from .serializers import FavoriteSerializer
from catalog.models import Product
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404

# Create your views here.

class FavoriteListView(generics.ListAPIView):
    serializer_class = FavoriteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)

class FavoriteAddView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        product_id = request.data.get('product_id')
        product = get_object_or_404(Product, id=product_id)
        favorite, created = Favorite.objects.get_or_create(user=request.user, product=product)
        if not created:
            return Response({'detail': 'Already in favorites.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(FavoriteSerializer(favorite).data, status=status.HTTP_201_CREATED)

class FavoriteDeleteView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, product_id):
        favorite = get_object_or_404(Favorite, user=request.user, product_id=product_id)
        favorite.delete()
        return Response({'detail': 'Removed from favorites.'}, status=status.HTTP_204_NO_CONTENT)
