from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

from authuser.models import User
from .forms import CustomUserCreationForm 

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

def password_reset(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            form.save(
                use_https=request.is_secure(),
                from_email=None,
                email_template_name='authuser/password_reset_email.html',
                subject_template_name='authuser/password_reset_subject.txt',
            )
            messages.success(request, 'Un email de réinitialisation a été envoyé.')
            return redirect('password_reset_done')
    else:
        form = PasswordResetForm()
    return render(request, 'authuser/password_reset.html', {'form': form})

# Vue après la demande de réinitialisation de mot de passe (notification envoyée)
def password_reset_done(request):
    return render(request, 'authuser/password_reset_done.html')

# Vue pour confirmer la réinitialisation de mot de passe
def password_reset_confirm(request, uidb64=None, token=None):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        if request.method == 'POST':
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'Votre mot de passe a été modifié avec succès.')
                return redirect('password_reset_complete')
        else:
            form = SetPasswordForm(user)
    else:
        messages.error(request, 'Le lien de réinitialisation est invalide.')

    return render(request, 'authuser/password_reset_confirm.html', {'form': form})

# Vue après la réinitialisation complète
def password_reset_complete(request):
    return render(request, 'authuser/password_reset_complete.html')