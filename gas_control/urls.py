from django.urls import path
from . import views

urlpatterns = [
    path('gas_control/', views.gases, name='gases'),
    path('', views.basic, name='home'),
    path('gas/', views.gases, name='gas'),
]
