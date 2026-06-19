from django.db import models
from django.conf import settings

class StudentProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    academic_level = models.CharField(max_length=100, blank=True, null=True)
    cgpa = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ielts_score = models.DecimalField(max_digits=3, decimal_places=1, blank=True, null=True)
    gre_score = models.IntegerField(blank=True, null=True)
    preferred_countries = models.JSONField(default=list, blank=True)
    budget = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    degree_preferences = models.CharField(max_length=255, blank=True, null=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - Profile"

    @property
    def completion_percentage(self):
        fields = [self.academic_level, self.cgpa, self.ielts_score, self.preferred_countries, self.budget, self.degree_preferences]
        filled = sum(1 for field in fields if field)
        return int((filled / len(fields)) * 100)
