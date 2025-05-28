from .models import Organization, Payment, BalanceLog
from django.db import transaction, IntegrityError


def process_payment(data):
    try:
        with transaction.atomic():
            payment = Payment.objects.create(**data)
            org, _ = Organization.objects.get_or_create(inn=data["payer_inn"])
            org.balance += data["amount"]
            org.save()
            BalanceLog.objects.create(organization=org, amount=data["amount"])
            print(f"Balance updated for {org.inn}: +{data['amount']}")
    except IntegrityError:
        print("Duplicate payment, skipping.")
