from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from .models import Customer, Account, Transaction
from .forms import CustomerForm, AccountForm, TransactionForm

def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'accounts/customer_list.html', {'customers': customers})

def account_detail(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    transactions = account.transactions.all().order_by('-created_at')
    return render(request, 'accounts/account_detail.html', {
        'account': account,
        'transactions': transactions
    })

def create_transaction(request, account_id):
    account = get_object_or_404(Account, id=account_id)
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.account = account
            transaction.save()
            return redirect('account_detail', account_id=account.id)
    else:
        form = TransactionForm()
    return render(request, 'accounts/create_transaction.html', {
        'form': form,
        'account': account
    })