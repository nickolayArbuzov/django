from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Organization
from django.shortcuts import get_object_or_404


class BalanceView(APIView):
    def get(self, request, inn):
        org = get_object_or_404(Organization, inn=inn)
        return Response({"inn": org.inn, "balance": org.balance})
