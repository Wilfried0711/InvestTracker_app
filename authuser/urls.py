from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from authuser.views import login,logout,register,password_reset_complete,password_reset,password_reset_confirm,password_reset_done

urlpatterns = [
    # Page de connexion
    path('login/', login , name='login'),
    
    # Page de déconnexion
    path('logout/', logout, name='logout'),

    # Page d'enregistrement (inscription)
    path('register/', register, name='register'),
    
    # Page de réinitialisation de mot de passe (optionnelle)
    path('password_reset/', password_reset , name='password_reset'),
    path('password_reset/done/', password_reset, name='password_reset_done'),
    path('reset/<uidb64>/<token>/', password_reset_confirm , name='password_reset_confirm'),
    path('reset/done/', password_reset_complete , name='password_reset_complete'),
]
