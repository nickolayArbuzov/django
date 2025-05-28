from django.urls import path
from .views import BankWebhookView

urlpatterns = [
    path("bank/", BankWebhookView.as_view()),
]
