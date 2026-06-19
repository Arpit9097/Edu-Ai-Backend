from django.db import models

class University(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    ranking = models.IntegerField(blank=True, null=True)
    tuition_fee = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    min_cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    min_ielts = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    min_gre = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Universities"

    def __str__(self):
        return self.name
