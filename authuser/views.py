from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from .forms import CustomUserCreationForm  # Assurez-vous d'avoir un formulaire personnalisé pour la création d'utilisateurs

# Vue pour l'enregistrement d'un nouvel utilisateur (register)
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Votre compte a été créé avec succès. Veuillez vous connecter.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authuser/register.html', {'form': form})

# Vue pour se connecter (login)
def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Rediriger vers la page d'accueil ou toute autre page après connexion
        else:
            messages.error(request, 'Email ou mot de passe incorrect.')
    return render(request, 'authuser/login.html')

# Vue pour se déconnecter (logout)
def logout_view(request):
    logout(request)
    messages.success(request, 'Vous avez été déconnecté avec succès.')
    return redirect('login')
