from django.urls import path
from . import views

urlpatterns = [
    path('', views.portfolio_list, name='portfolio_list'),
    path('create/', views.create_portfolio, name='create_portfolio'),
]
