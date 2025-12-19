from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class SalesListCreateView(APIView):
    def get(self, request):
        return Response({"message": "GET sales works!"}, status=status.HTTP_200_OK)

    def post(self, request):
        return Response({"message": "POST sales works!"}, status=status.HTTP_201_CREATED)

def index(request):
    return HttpResponse("Sales app is working!")
