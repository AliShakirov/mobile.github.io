from django.urls import path
from .views import CartView, CartItemAddView, CartItemUpdateDeleteView

urlpatterns = [
    path('', CartView.as_view(), name='cart'),
    path('add/', CartItemAddView.as_view(), name='cart-add'),
    path('item/<int:item_id>/', CartItemUpdateDeleteView.as_view(), name='cart-item-update-delete'),
] 