from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import PurchaseViewSet, PurchaseListCreateView, index

router = DefaultRouter()
router.register(r'purchase', PurchaseViewSet, basename='purchase')

urlpatterns = [
    # Use router URLs for CRUD
    path('', include(router.urls)),

    # Optional test endpoint
    path('test/', index, name='purchase-index'),

    # Optional standalone list/create view
    path('list-create/', PurchaseListCreateView.as_view(), name='purchase-list-create'),
]
