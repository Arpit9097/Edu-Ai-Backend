from django.urls import path
from .views import RecommendationListView, GenerateRecommendationsView

urlpatterns = [
    path('', RecommendationListView.as_view(), name='recommendation_list'),
    path('generate/', GenerateRecommendationsView.as_view(), name='recommendation_generate'),
]
