# StockHub/urls.py
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.contrib.auth.views import LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

def root_test(request):
    return HttpResponse("Root URL works")

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Root test
    path('', root_test, name='root'),

    # User authentication endpoints
    path('api/auth/login/', obtain_auth_token, name='api_token_auth'),  # Token auth
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # App endpoints
    path('api/accounts/', include('accounts.urls')),  # user management
    path('api/inventory/', include('inventory.urls')),
    path('api/purchases/', include('purchase.urls')),
    path('api/sales/', include('sales.urls')),
]
