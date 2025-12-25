from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from rest_framework.permissions import AllowAny

from .models import Sales
from .serializers import SalesSerializer


class SalesViewSet(viewsets.ModelViewSet):
    """
    CRUD operations for Sales model
    """
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [AllowAny]


class SalesListCreateView(APIView):
    """
    Handle listing and creating sales records (test endpoint)
    """
    permission_classes = [AllowAny]

    def get(self, request):
        return Response(
            {"message": "GET sales works!"},
            status=status.HTTP_200_OK
        )

    def post(self, request):
        data = request.data
        return Response(
            {
                "message": "POST sales works!",
                "data_received": data
            },
            status=status.HTTP_201_CREATED
        )


def index(request):
    return HttpResponse("Sales app is working!")
