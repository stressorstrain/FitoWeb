from django.urls import path
from . import views

urlpatterns = [
    path('', views.gases, name='gases'),

]
