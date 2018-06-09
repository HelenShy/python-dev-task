from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets, status, generics, filters, permissions as prm
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Agreement, Payment
from .serializers import PaymentSerializer, AgreementSerializer


class AgreementsViewSet(viewsets.ViewSet):
    """
    Retrieves agreements from json file.
    """
    serializer_class = AgreementSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, pk):
        agreement = Agreement.objects.by_id(int(pk))
        serializer = AgreementSerializer(agreement, many=False)
        return Response(serializer.data)

    def list(self, request):
        agreements = Agreement.objects.all()
        serializer = AgreementSerializer(agreements, many=True)
        return Response(serializer.data)


class PaymentsViewSet(viewsets.ViewSet):
    """
    Retrieves payments from json file.
    """
    serializer_class = PaymentSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, )

    def retrieve(self, request, agreement_pk=None, pk=None):
        payment = Payment.objects.by_id(agreement_pk, pk)
        serializer = PaymentSerializer(payment, many=False)
        return Response(serializer.data)

    def list(self, request, agreement_pk=None):
        payments = Payment.objects.by_agreement_id(agreement_pk)
        serializer = PaymentSerializer(payments, many=True)
        return Response(serializer.data)
