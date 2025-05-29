from django.db import transaction, IntegrityError
from .models import Payment, BalanceLog
from organizations.models import Organization


class BankWebhookService:
    def __init__(self, data: dict):
        self.data = data

    def process(self):
        try:
            with transaction.atomic():
                self._create_payment()
                org = self._get_or_create_organization()
                self._update_balance(org)
                self._create_balance_log(org)
                print(f"Updated balance for {org.inn}: +{self.data['amount']}")
        except IntegrityError:
            print("Duplicate operation_id. Skipping.")

    def _create_payment(self):
        Payment.objects.create(**self.data)

    def _get_or_create_organization(self):
        org, _ = Organization.objects.get_or_create(inn=self.data["payer_inn"])
        return org

    def _update_balance(self, org):
        org.balance += self.data["amount"]
        org.save()

    def _create_balance_log(self, org):
        BalanceLog.objects.create(organization=org, amount=self.data["amount"])
