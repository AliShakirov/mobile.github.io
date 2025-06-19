from django.urls import path
from .views import DeliveryInfoDetailView

urlpatterns = [
    path('<int:pk>/', DeliveryInfoDetailView.as_view(), name='delivery-detail'),
] 