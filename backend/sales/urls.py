from django.urls import path
from .views import SaleListView, SaleDetailView

urlpatterns = [
    path('', SaleListView.as_view(), name='sale-list'),
    path('<int:pk>/', SaleDetailView.as_view(), name='sale-detail'),
] 