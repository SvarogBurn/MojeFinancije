import factory
import decimal
from factory.django import DjangoModelFactory
from main.models import *

class AccountFactory(DjangoModelFactory):
    class Meta:
        model = Account

    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    iban = factory.Faker("pystr", max_chars=21)
    balance = factory.Faker("pydecimal", min_value=1, max_value=10000)
    account_created = factory.Faker("date_time")


class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker("name")
    description = factory.Faker("sentence", nb_words=15)
    

class TransactionFactory(DjangoModelFactory):
    class Meta:
        model = Transaction

    account = factory.Iterator(Account.objects.all())
    category = factory.Iterator(Category.objects.all())
    amount = factory.Faker("pydecimal", min_value=1, max_value=10000)
    description = factory.Faker("sentence", nb_words=15)
    transaction_date = factory.Faker("date_time")    
    is_income = True