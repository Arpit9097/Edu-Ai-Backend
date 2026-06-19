from django.db import models
from django.conf import settings

class LoanQuery(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='loan_queries')
    loan_amount = models.DecimalField(max_digits=12, decimal_places=2)
    interest_rate = models.DecimalField(max_digits=5, decimal_places=2)
    tenure = models.IntegerField(help_text="Tenure in months")
    
    emi = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_interest = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    total_repayment = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Loan Queries"

    def __str__(self):
        return f"{self.user.email} - {self.loan_amount} @ {self.interest_rate}%"
