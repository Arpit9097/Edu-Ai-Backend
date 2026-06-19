from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import University
from .serializers import UniversitySerializer

class UniversityListView(generics.ListAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny] # Can be changed to IsAuthenticated if required
    
class UniversityDetailView(generics.RetrieveAPIView):
    queryset = University.objects.all()
    serializer_class = UniversitySerializer
    permission_classes = [AllowAny]
