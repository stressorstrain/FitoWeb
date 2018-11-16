from django.urls import path
from accounts import views

app_name = 'accounts'
urlpatterns = [
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('userc/', views.register, name='userc'),
    path('', views.log_in, name='log_in'),

    path('<str:username>', views.profile, name='profilepage'),

    path('accounts/notes/delete/<int:pk>', views.DeleteNote.as_view(), name='note_delete'),
    path('accounts/projects/delete/<int:pk>', views.DeleteProject.as_view(), name='proj_delete'),
]
