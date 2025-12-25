from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SalesViewSet, SalesListCreateView, index

# Create a router and register the ViewSet
router = DefaultRouter()
router.register(r"sales", SalesViewSet, basename="sales")  # this enables /api/sales/sales/

urlpatterns = [
    # Class-based test API
    path("", SalesListCreateView.as_view(), name="sales-list-create"),

    # Simple test page
    path("test/", index, name="sales-test"),

    # Include the router URLs (CRUD)
    path("", include(router.urls)),
]
