from rest_framework import serializers
from .models import LoanQuery

class LoanQuerySerializer(serializers.ModelSerializer):
    class Meta:
        model = LoanQuery
        fields = '__all__'
        read_only_fields = ('user', 'emi', 'total_interest', 'total_repayment')
