from django.urls import path
from . import views

urlpatterns = [
    path('', views.company_list, name='company_list'),
    path('companies/', views.company_list, name='company_list'),
    path('companies/create/', views.create_company, name='create_company'),
    path('companies/<int:pk>/edit/', views.update_company, name='update_company'),
    path('companies/<int:pk>/delete/', views.delete_company, name='delete_company'),
]
