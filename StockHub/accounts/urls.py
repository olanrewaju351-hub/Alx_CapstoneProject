# accounts/urls.py
from django.urls import path
from . import views
from .views import home
from .views import RegisterView, LoginView, LogoutView, ProfileView
from .views import StockListCreateView, StockRetrieveUpdateDestroyView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', home, name='home'),
    path('stock/', StockListCreateView.as_view(), name='stock-list-create'),
    path('stock/<int:id>/', StockRetrieveUpdateDestroyView.as_view(), name='stock-detail'),
]
