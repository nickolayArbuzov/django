from django.shortcuts import get_object_or_404
from organizations.models import Organization


class BalanceService:
    def __init__(self, inn: str):
        self.inn = inn

    def get_balance(self):
        org = get_object_or_404(Organization, inn=self.inn)
        return {"inn": org.inn, "balance": org.balance}
