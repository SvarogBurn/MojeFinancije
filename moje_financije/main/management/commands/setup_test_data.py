import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import *
from main.factories import *

NUM_ACCOUNTS = 10
NUM_CATEGORIES = 5
NUM_TRANSACTIONS = 100

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Account, Category, Transaction]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_ACCOUNTS):
            account = AccountFactory()

        for _ in range(NUM_CATEGORIES):
            category = CategoryFactory()
            
        for _ in range(NUM_TRANSACTIONS):
            transaction = TransactionFactory()