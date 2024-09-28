from django import forms
from .models import FinancialDocument

class FinancialDocumentForm(forms.ModelForm):
    class Meta:
        model = FinancialDocument
        fields = ['company', 'document']  # Les champs à inclure dans le formulaire
        widgets = {
            'company': forms.Select(attrs={'class': 'form-control'}),
            'document': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

    # Méthode pour ajouter une validation personnalisée sur le fichier
    def clean_document(self):
        document = self.cleaned_data.get('document')

        if document:
            if document.size > 5 * 1024 * 1024:  # Limite de 5MB
                raise forms.ValidationError("Le fichier est trop volumineux (maximum 5MB).")
            return document
