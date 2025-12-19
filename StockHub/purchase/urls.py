from django.urls import path
from .views import PurchaseListCreateView, index

urlpatterns = [
    path('', PurchaseListCreateView.as_view(), name='purchase-list-create'),
    path('test/', index, name='purchase-index'),
]
