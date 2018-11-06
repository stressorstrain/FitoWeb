from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('userc/', views.register, name='userc'),
    path('', views.log_in, name='log_in'),
    path('<str:username>', views.profile, name='profilepage'),
]
