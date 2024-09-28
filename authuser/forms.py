from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

# Formulaire pour la création d'un nouvel utilisateur
class CustomUserCreationForm(UserCreationForm):
    password1 = forms.CharField(label='Mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='Confirmation du mot de passe', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('email', 'name')  # Champs affichés lors de la création d'un utilisateur
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
        }

    # Validation pour vérifier que les deux mots de passe sont identiques
    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return password2

    # Méthode pour sauvegarder l'utilisateur avec un mot de passe chiffré
    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user

# Formulaire pour la modification d'un utilisateur existant (utilisé dans l'administration ou par l'utilisateur lui-même)
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('email', 'name', 'is_active', 'is_staff', 'is_superuser')  # Champs modifiables par un admin
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_staff': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'is_superuser': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
