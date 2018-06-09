from rest_framework import serializers
from .models import Payment, Agreement


class AgreementSerializer(serializers.ModelSerializer):
    """
    Serializes user profile feed items.
    """
    class Meta:
        model = Agreement
        fields = ('id',)


class PaymentSerializer(serializers.ModelSerializer):
    """
    Serializes user profile feed items.
    """
    class Meta:
        model = Payment
        fields = ('id', 'agreement', 'amount', 'date')
        depth = 0
