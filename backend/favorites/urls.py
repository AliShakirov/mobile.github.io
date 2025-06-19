from django.urls import path
from .views import FavoriteListView, FavoriteAddView, FavoriteDeleteView

urlpatterns = [
    path('', FavoriteListView.as_view(), name='favorite-list'),
    path('add/', FavoriteAddView.as_view(), name='favorite-add'),
    path('delete/<int:product_id>/', FavoriteDeleteView.as_view(), name='favorite-delete'),
] 