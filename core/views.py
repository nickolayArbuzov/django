from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .serializers import BankWebhookSerializer
from .services import process_payment
from .models import Organization


class BankWebhookView(APIView):
    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        process_payment(serializer.validated_data)
        return Response(status=status.HTTP_200_OK)


class BalanceView(APIView):
    def get(self, request, inn):
        org = get_object_or_404(Organization, inn=inn)
        return Response({"inn": org.inn, "balance": org.balance})
