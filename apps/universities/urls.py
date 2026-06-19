from django.urls import path
from .views import UniversityListView, UniversityDetailView

urlpatterns = [
    path('', UniversityListView.as_view(), name='university_list'),
    path('<int:pk>/', UniversityDetailView.as_view(), name='university_detail'),
]
