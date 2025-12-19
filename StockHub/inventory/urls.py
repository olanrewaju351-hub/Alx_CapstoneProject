from django.urls import path
from .views import InventoryListCreateView, index

urlpatterns = [
    path('', InventoryListCreateView.as_view(), name='inventory-list-create'),
    path('test/', index, name='inventory-index'),
]
