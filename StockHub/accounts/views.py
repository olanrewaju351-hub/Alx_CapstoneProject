# accounts/views.py
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    # If you have the template at accounts/templates/accounts/home.html use the render line:
    return render(request, 'accounts/home.html')

    # If you prefer a quick text response (no template), comment the render above and use:
    # return HttpResponse("Hello — StockHub home page is working")
