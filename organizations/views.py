from rest_framework.views import APIView
from rest_framework.response import Response
from .services import BalanceService


class BalanceView(APIView):
    def get(self, request, inn):
        service = BalanceService(inn)
        balance_data = service.get_balance()
        return Response(balance_data)
