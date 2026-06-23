from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse


def home(request):
    return JsonResponse({
        "message": "EduAI backend is running successfully"
    })


urlpatterns = [
    path('', home),

    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
    path('api/profile/', include('apps.profiles.urls')),
    path('api/universities/', include('apps.universities.urls')),
    path('api/recommendations/', include('apps.recommendations.urls')),
    path('api/loans/', include('apps.loans.urls')),
    path('api/chat/', include('apps.chat.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
]