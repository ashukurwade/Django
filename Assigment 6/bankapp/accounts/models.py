from django.db import models

# Create your models here.
from django.core.validators import MinValueValidator

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    ACCOUNT_TYPES = [
        ('SAVINGS', 'Savings'),
        ('CHECKING', 'Checking'),
        ('BUSINESS', 'Business'),
    ]
    
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='accounts')
    balance = models.DecimalField(max_digits=12, decimal_places=2, default=0.00, validators=[MinValueValidator(0)])
    account_type = models.CharField(max_length=10, choices=ACCOUNT_TYPES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.account_type} Account - {self.customer}"

class Transaction(models.Model):
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'Deposit'),
        ('WITHDRAWAL', 'Withdrawal'),
    ]
    
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='transactions')
    transaction_type = models.CharField(max_length=10, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0.01)])
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.transaction_type} of ${self.amount} on {self.created_at}"
    
    def save(self, *args, **kwargs):
        # Update account balance when transaction is saved
        if not self.pk:  # Only for new transactions
            if self.transaction_type == 'DEPOSIT':
                self.account.balance += self.amount
            else:  # WITHDRAWAL
                if self.amount > self.account.balance:
                    raise ValueError("Insufficient funds")
                self.account.balance -= self.amount
            self.account.save()
        super().save(*args, **kwargs)