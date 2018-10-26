from django.urls import path
from . import views

urlpatterns = [
    path('', views.basic, name='home'),
    path('gas_control/', views.gases, name='gases'),
    path('chart/', views.chart, name='chart'),
    #path('mplimage/', views.charts),
    path('userc/', views.register, name='userc')

    #path('gas_control/', views.test, name='test'),
]
