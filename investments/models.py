from django.db import models
from portfolios.models import Portfolio

class Investment(models.Model):
    INVESTMENT_TYPE_CHOICES = [
        ('action', 'Action'),
        ('obligation', 'Obligation'),
    ]
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    investment_type = models.CharField(max_length=20, choices=INVESTMENT_TYPE_CHOICES)
    quantity = models.IntegerField()
    current_value = models.FloatField()

    def __str__(self):
        return f'{self.investment_type} - {self.quantity}'
