from django.db import models

class Account(models.Model):
    """Model koji predstavlja korisnički račun."""
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    """Model za kategorije transakcija."""
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    is_income = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Transaction(models.Model):
    """Model za transakcije."""
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.amount} - {self.category} ({self.date})"
