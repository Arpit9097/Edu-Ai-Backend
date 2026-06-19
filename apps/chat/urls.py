from django.urls import path
from .views import ChatSessionListView, ChatMessageCreateView

urlpatterns = [
    path('', ChatMessageCreateView.as_view(), name='chat_message_create'),
    path('history/', ChatSessionListView.as_view(), name='chat_history'),
]
