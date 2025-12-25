from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, filters
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Stock
from .serializers import StockSerializer


class StockViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Stock model
    """
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    permission_classes = [AllowAny]
    filter_backends = [filters.SearchFilter]
    search_fields = ['item_code', 'warehouse']


@api_view(["GET"])
@permission_classes([AllowAny])
def inventory_search(request):
    """
    Search inventory using query parameters
    Example:
    /api/inventory/search/?item_code=ABC123&warehouse=Main
    """
    item_code = request.query_params.get("item_code")
    warehouse = request.query_params.get("warehouse")

    queryset = Stock.objects.all()
    if item_code:
        queryset = queryset.filter(item_code__icontains=item_code)
    if warehouse:
        queryset = queryset.filter(warehouse__icontains=warehouse)

    serializer = StockSerializer(queryset, many=True)
    return Response(
        {
            "results": serializer.data,
            "message": "Inventory search endpoint is working"
        },
        status=status.HTTP_200_OK
    )


class InventoryListCreateView(APIView):
    """
    Simple inventory test endpoint
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"message": "GET inventory works!"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST inventory works!"}, status=status.HTTP_201_CREATED)


def index(request):
    return HttpResponse("Inventory app is working!")
