from django.shortcuts import render, redirect
from .models import FinancialDocument
from .forms import FinancialDocumentForm

def upload_document(request, company_id):
    if request.method == 'POST':
        form = FinancialDocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.company_id = company_id
            document.save()
            return redirect('company_list')
    else:
        form = FinancialDocumentForm()
    return render(request, 'upload_document.html', {'form': form})
