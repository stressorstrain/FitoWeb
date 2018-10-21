from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic, name='home'),
    path('gas_control/', views.gases, name='gases'),
    path('chart/', views.chart, name='chart'),
    path('chart/api/', views.get_data, name='chart-api')

    #path('gas_control/', views.test, name='test'),
]
