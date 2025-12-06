# accounts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),      # root of site => accounts.views.home
    # add other routes as needed
]
