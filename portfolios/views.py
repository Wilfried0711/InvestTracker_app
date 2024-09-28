from django.shortcuts import render, redirect
from .models import Portfolio

def portfolio_list(request):
    portfolios = Portfolio.objects.filter(user=request.user)
    return render(request, 'portfolio_list.html', {'portfolios': portfolios})

def create_portfolio(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        Portfolio.objects.create(user=request.user, name=name)
        return redirect('portfolio_list')
    return render(request, 'create_portfolio.html')
