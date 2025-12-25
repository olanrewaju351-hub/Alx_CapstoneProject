from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from .models import Purchase
from .serializers import PurchaseSerializer


class PurchaseViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Purchase model
    """
    queryset = Purchase.objects.all()
    serializer_class = PurchaseSerializer
    permission_classes = [AllowAny]


class PurchaseListCreateView(APIView):
    """
    Handle listing and creating purchases (validated)
    """
    permission_classes = [AllowAny]

    def get(self, request):
        purchases = Purchase.objects.all()
        serializer = PurchaseSerializer(purchases, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = PurchaseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {
                    "message": "POST purchase works!",
                    "data_saved": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        # Return validation errors if any required fields are missing or invalid
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def index(request):
    return HttpResponse("Purchase app is working!")
