from django import forms
from .models import Customer, Account, Transaction

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'email', 'phone']

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['customer', 'account_type']

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['transaction_type', 'amount']