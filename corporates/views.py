from django.shortcuts import render, get_object_or_404, redirect
from .models import Company
from .forms import CompanyForm

# Create (ajouter une nouvelle entreprise)
def create_company(request):
    if request.method == 'POST':
        form = CompanyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm()
    return render(request, 'company/create_company.html', {'form': form})

# Read (liste des entreprises)
def company_list(request):
    companies = Company.objects.all()
    return render(request, 'company/company_list.html', {'companies': companies})

# Update (mise à jour d'une entreprise)
def update_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        form = CompanyForm(request.POST, instance=company)
        if form.is_valid():
            form.save()
            return redirect('company_list')
    else:
        form = CompanyForm(instance=company)
    return render(request, 'company/update_company.html', {'form': form, 'company': company})

# Delete (suppression d'une entreprise)
def delete_company(request, pk):
    company = get_object_or_404(Company, pk=pk)
    if request.method == 'POST':
        company.delete()
        return redirect('company_list')
    return render(request, 'company/delete_company.html', {'company': company})
