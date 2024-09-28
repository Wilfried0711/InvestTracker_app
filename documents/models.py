from django.db import models
from corporates.models import Company

class FinancialDocument(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Document for {self.company.name}'
