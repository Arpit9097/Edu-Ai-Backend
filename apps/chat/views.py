from django.conf import settings
from rest_framework import views, status, generics
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import ChatSession, ChatMessage
from .serializers import ChatSessionSerializer
from .groq_service import GroqService

# Initialize GroqService
groq_service = GroqService()

class ChatSessionListView(generics.ListAPIView):
    serializer_class = ChatSessionSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return ChatSession.objects.filter(user=self.request.user).order_by('-created_at')

class ChatMessageCreateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        message_content = request.data.get('message')
        session_id = request.data.get('session_id')

        if not message_content:
            return Response({"error": "Message content is required"}, status=status.HTTP_400_BAD_REQUEST)

        if session_id:
            try:
                session = ChatSession.objects.get(id=session_id, user=user)
            except ChatSession.DoesNotExist:
                return Response({"error": "Session not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            session = ChatSession.objects.create(user=user, title=message_content[:50])

        # Save user message
        ChatMessage.objects.create(session=session, role='user', content=message_content)

        # Call Groq AI
        try:
            ai_reply = groq_service.generate_chat_response(session)
            ChatMessage.objects.create(session=session, role='ai', content=ai_reply)

            return Response({
                "session_id": session.id,
                "reply": ai_reply
            }, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
