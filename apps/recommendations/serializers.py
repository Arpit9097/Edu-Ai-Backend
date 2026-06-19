from rest_framework import serializers
from .models import Recommendation
from apps.universities.serializers import UniversitySerializer

class RecommendationSerializer(serializers.ModelSerializer):
    university_details = UniversitySerializer(source='university', read_only=True)

    class Meta:
        model = Recommendation
        fields = '__all__'
        read_only_fields = ('user', 'university_details', 'match_percentage')
