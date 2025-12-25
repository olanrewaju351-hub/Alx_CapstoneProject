from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    inventory_search,
    InventoryListCreateView,
    index,
    StockViewSet,
)

router = DefaultRouter()
router.register(r"stocks", StockViewSet, basename="stock")  # CRUD endpoints: /stocks/

urlpatterns = [
    # ViewSet (CRUD) – should come first to avoid conflicts with empty path
    path("", include(router.urls)),

    # Class-based test API
    path("list-create/", InventoryListCreateView.as_view(), name="inventory-list-create"),

    # Function-based search endpoint
    path("search/", inventory_search, name="inventory-search"),

    # Simple test endpoint
    path("test/", index, name="inventory-index"),
]
