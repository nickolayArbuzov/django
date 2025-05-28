from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import BankWebhookSerializer
from .services import process_webhook


class BankWebhookView(APIView):
    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        process_webhook(serializer.validated_data)
        return Response(status=status.HTTP_200_OK)
