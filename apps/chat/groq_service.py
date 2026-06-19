import logging
from django.conf import settings
from groq import Groq

logger = logging.getLogger(__name__)

class GroqService:
    def __init__(self):
        self.api_key = getattr(settings, 'GROQ_API_KEY', None)
        if not self.api_key or self.api_key == "your_api_key":
            logger.warning("GROQ_API_KEY is not set or is using the default placeholder value in settings.")
            # Fallback to direct environment check
            import os
            self.api_key = os.getenv("GROQ_API_KEY")
        
        self.client = Groq(api_key=self.api_key)
        self.model = 'llama-3.3-70b-versatile'

    def generate_chat_response(self, session):
        """
        Fetches the chat message history for the given session from the database,
        formats it for Groq, and generates a response.
        """
        try:
            from .models import ChatMessage
            
            # Fetch all messages in this session ordered by creation time
            history = ChatMessage.objects.filter(session=session).order_by('created_at')
            
            # Initialize with system instructions
            messages = [
                {
                    "role": "system",
                    "content": "You are EduAI, an expert student advisor assisting students with university searches, profile optimization, loans, and other chat queries."
                }
            ]
            
            # Format and append previous chat messages
            for msg in history:
                role = 'user' if msg.role == 'user' else 'assistant'
                messages.append({
                    "role": role,
                    "content": msg.content
                })
            
            # Call Groq API
            chat_completion = self.client.chat.completions.create(
                messages=messages,
                model=self.model,
            )
            
            ai_reply = chat_completion.choices[0].message.content
            return ai_reply.strip()
            
        except Exception as e:
            logger.error(f"Error during Groq chat completion call: {str(e)}")
            return "I'm sorry, but I am experiencing issues communicating with my AI backend. Please try again later."
