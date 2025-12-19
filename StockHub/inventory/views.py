from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# DRF API view
class InventoryListCreateView(APIView):
    def get(self, request):
        return Response({"message": "GET inventory works!"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST inventory works!"}, status=status.HTTP_201_CREATED)

# Browser test view
def index(request):
    return HttpResponse("Inventory app is working!")
