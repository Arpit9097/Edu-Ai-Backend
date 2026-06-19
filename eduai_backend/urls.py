from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('apps.users.urls')),
    path('api/profile/', include('apps.profiles.urls')),
    path('api/universities/', include('apps.universities.urls')),
    path('api/recommendations/', include('apps.recommendations.urls')),
    path('api/loans/', include('apps.loans.urls')),
    path('api/chat/', include('apps.chat.urls')),
    path('api/dashboard/', include('apps.dashboard.urls')),
]
