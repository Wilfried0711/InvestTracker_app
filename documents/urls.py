from django.urls import path
from . import views

urlpatterns = [
    path('upload/<int:company_id>/', views.upload_document, name='upload_document'),
]
