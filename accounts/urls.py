from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('userc/', views.register, name='userc'),
    path('', views.basic, name='homepage')

]
