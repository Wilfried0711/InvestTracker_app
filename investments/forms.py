from django import forms
from .models import Investment

class InvestmentForm(forms.ModelForm):
    class Meta:
        model = Investment
        fields = ['portfolio', 'investment_type', 'quantity', 'current_value']  # Champs du formulaire
        widgets = {
            'portfolio': forms.Select(attrs={'class': 'form-control'}),
            'investment_type': forms.Select(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'current_value': forms.NumberInput(attrs={'class': 'form-control'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity <= 0:
            raise forms.ValidationError("La quantité doit être supérieure à zéro.")
        return quantity

    def clean_current_value(self):
        current_value = self.cleaned_data.get('current_value')
        if current_value <= 0:
            raise forms.ValidationError("La valeur actuelle doit être supérieure à zéro.")
        return current_value
