from django.shortcuts import render, get_object_or_404, redirect
from .models import Investment
from .forms import InvestmentForm  # Assurez-vous d'avoir un formulaire dans forms.py
from django.contrib import messages

# Vue pour afficher la liste des investissements (Lire)
def investment_list(request):
    investments = Investment.objects.all()  # Récupère tous les investissements
    return render(request, 'investment/investment_list.html', {'investments': investments})

# Vue pour créer un nouvel investissement (Créer)
def investment_create(request):
    if request.method == 'POST':
        form = InvestmentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'investissement a été créé avec succès.')
            return redirect('investment_list')
    else:
        form = InvestmentForm()
    return render(request, 'investment/investment_form.html', {'form': form})

# Vue pour mettre à jour un investissement (Mettre à jour)
def investment_update(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        form = InvestmentForm(request.POST, instance=investment)
        if form.is_valid():
            form.save()
            messages.success(request, 'L\'investissement a été mis à jour avec succès.')
            return redirect('investment_list')
    else:
        form = InvestmentForm(instance=investment)
    return render(request, 'investment/investment_form.html', {'form': form})

# Vue pour supprimer un investissement (Supprimer)
def investment_delete(request, id):
    investment = get_object_or_404(Investment, id=id)
    if request.method == 'POST':
        investment.delete()
        messages.success(request, 'L\'investissement a été supprimé avec succès.')
        return redirect('investment_list')
    return render(request, 'investment/investment_confirm_delete.html', {'investment': investment})
