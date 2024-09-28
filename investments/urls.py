from django.urls import path
from . import views

urlpatterns = [
    path('', views.investment_list, name='investment_list'),
    path('create/', views.investment_create, name='investment_create'),
    path('update/<int:id>/', views.investment_update, name='investment_update'),
    path('delete/<int:id>/', views.investment_delete, name='investment_delete'),
]
