from django.urls import path
from .views import LoanCalculateView, LoanHistoryView

urlpatterns = [
    path('calculate/', LoanCalculateView.as_view(), name='loan_calculate'),
    path('history/', LoanHistoryView.as_view(), name='loan_history'),
]
