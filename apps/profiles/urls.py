from django.urls import path
from .views import StudentProfileView

urlpatterns = [
    path('', StudentProfileView.as_view(), name='profile_detail'),
    path('update/', StudentProfileView.as_view(), name='profile_update'),
]
