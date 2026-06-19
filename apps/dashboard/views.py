from rest_framework import views, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from apps.profiles.models import StudentProfile
from apps.recommendations.models import Recommendation
from apps.chat.models import ChatSession

class DashboardStatsView(views.APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        
        # Profile completion
        try:
            profile = user.profile
            completion_percentage = profile.completion_percentage
        except StudentProfile.DoesNotExist:
            completion_percentage = 0

        # Recommendation count
        recommendation_count = Recommendation.objects.filter(user=user).count()

        # Recent chats
        recent_chats = ChatSession.objects.filter(user=user).order_by('-created_at')[:5]
        chats_data = [{"id": chat.id, "title": chat.title, "date": chat.created_at} for chat in recent_chats]

        # Readiness score (mock calculation)
        readiness_score = int(completion_percentage * 0.8 + (10 if recommendation_count > 0 else 0))

        return Response({
            "profile_completion_percentage": completion_percentage,
            "application_readiness_score": readiness_score,
            "recommendation_count": recommendation_count,
            "recent_chats": chats_data
        }, status=status.HTTP_200_OK)
