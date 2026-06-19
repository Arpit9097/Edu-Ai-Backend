from rest_framework import generics, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import LoanQuery
from .serializers import LoanQuerySerializer
from decimal import Decimal

class LoanCalculateView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = LoanQuerySerializer(data=request.data)
        if serializer.is_valid():
            loan_amount = Decimal(serializer.validated_data['loan_amount'])
            interest_rate = Decimal(serializer.validated_data['interest_rate'])
            tenure_months = serializer.validated_data['tenure']

            # EMI Calculation: P * R * (1+R)^N / ((1+R)^N - 1)
            monthly_rate = interest_rate / (12 * 100)
            
            if monthly_rate > 0:
                emi = loan_amount * monthly_rate * ((1 + monthly_rate) ** tenure_months) / (((1 + monthly_rate) ** tenure_months) - 1)
            else:
                emi = loan_amount / tenure_months

            total_repayment = emi * tenure_months
            total_interest = total_repayment - loan_amount

            loan_query = serializer.save(
                user=request.user,
                emi=round(emi, 2),
                total_repayment=round(total_repayment, 2),
                total_interest=round(total_interest, 2)
            )
            
            response_data = LoanQuerySerializer(loan_query).data
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoanHistoryView(generics.ListAPIView):
    serializer_class = LoanQuerySerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return LoanQuery.objects.filter(user=self.request.user).order_by('-created_at')
