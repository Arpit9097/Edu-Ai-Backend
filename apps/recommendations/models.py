from django.db import models
from django.conf import settings
from apps.universities.models import University

class Recommendation(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='recommendations')
    university = models.ForeignKey(University, on_delete=models.CASCADE, related_name='recommended_for')
    match_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.email} - {self.university.name} ({self.match_percentage}%)"
