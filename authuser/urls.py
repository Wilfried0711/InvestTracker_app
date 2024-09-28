from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Page de connexion
    path('login/', auth_views.LoginView.as_view(template_name='authuser/login.html'), name='login'),
    
    # Page de déconnexion
    path('logout/', auth_views.LogoutView.as_view(template_name='authuser/logout.html'), name='logout'),

    # Page d'enregistrement (inscription)
    path('register/', views.register, name='register'),
    
    # Page de réinitialisation de mot de passe (optionnelle)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='authuser/password_reset.html'), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='authuser/password_reset_done.html'), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='authuser/password_reset_confirm.html'), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='authuser/password_reset_complete.html'), name='password_reset_complete'),
]
