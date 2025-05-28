from .models import Payment, BalanceLog
from organizations.models import Organization
from django.db import transaction, IntegrityError


def process_webhook(data: dict):
    try:
        with transaction.atomic():
            payment = Payment.objects.create(**data)
            org, _ = Organization.objects.get_or_create(inn=data["payer_inn"])
            org.balance += data["amount"]
            org.save()
            BalanceLog.objects.create(organization=org, amount=data["amount"])
            print(f"Updated balance for {org.inn}: +{data['amount']}")
    except IntegrityError:
        print("Duplicate operation_id. Skipping.")
