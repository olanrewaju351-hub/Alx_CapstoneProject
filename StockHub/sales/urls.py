from django.urls import path
from .views import SalesListCreateView, index
from . import views

urlpatterns = [
    path('', SalesListCreateView.as_view(), name='sales-list-create'),
    path('', views.index, name='sales-home'),
    path('test/', index, name='sales-index'),  # simple browser test
]
