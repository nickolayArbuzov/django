from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from .serializers import BankWebhookSerializer
from .services import BankWebhookService


class BankWebhookView(APIView):
    @swagger_auto_schema(
        request_body=BankWebhookSerializer,
        responses={201: "Created"},
    )
    def post(self, request):
        serializer = BankWebhookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        service = BankWebhookService(serializer.validated_data)
        service.process()
        return Response(status=status.HTTP_201_CREATED)
