from rest_framework import generics, views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Recommendation
from apps.universities.models import University
from apps.profiles.models import StudentProfile
from .serializers import RecommendationSerializer
from decimal import Decimal

class RecommendationListView(generics.ListAPIView):
    serializer_class = RecommendationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Recommendation.objects.filter(user=self.request.user).order_by('-match_percentage')

class GenerateRecommendationsView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        try:
            profile = user.profile
        except StudentProfile.DoesNotExist:
            return Response({"error": "Profile not found"}, status=status.HTTP_404_NOT_FOUND)

        # Basic mock recommendation engine logic
        universities = University.objects.all()
        Recommendation.objects.filter(user=user).delete() # Clear old ones
        
        recs = []
        for uni in universities:
            match_score = 100
            if profile.cgpa and uni.min_cgpa and profile.cgpa < uni.min_cgpa:
                match_score -= 30
            if profile.ielts_score and uni.min_ielts and profile.ielts_score < uni.min_ielts:
                match_score -= 20
            if profile.gre_score and uni.min_gre and profile.gre_score < uni.min_gre:
                match_score -= 20
            if profile.budget and uni.tuition_fee and profile.budget < uni.tuition_fee:
                match_score -= 30
                
            match_score = max(0, match_score)
            if match_score > 0:
                recs.append(Recommendation(user=user, university=uni, match_percentage=Decimal(match_score)))
                
        Recommendation.objects.bulk_create(recs)
        
        queryset = Recommendation.objects.filter(user=user).order_by('-match_percentage')
        serializer = RecommendationSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
