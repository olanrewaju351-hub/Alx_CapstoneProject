# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse

# DRF imports (used for LogoutView)
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework.authtoken.models import Token


def home(request):
    """
    Renders the app home page.
    Template path expected: accounts/templates/accounts/home.html
    """
    return render(request, 'accounts/home.html')
    # If you want a quick text-only response instead of a template, use:
    # return HttpResponse("Hello — StockHub home page is working")


class LogoutView(APIView):
    """
    Simple token-based logout view.
    Requires rest_framework.authtoken and the user to be authenticated.
    POST to this endpoint will delete the user's token (forcing re-login).
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, format=None):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
        except Token.DoesNotExist:
            # If token doesn't exist, that's fine — just return success
            pass
        return Response({"detail": "Logged out."}, status=status.HTTP_200_OK)
