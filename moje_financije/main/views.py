from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from main.models import Account, Category, Transaction
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, 'main/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

# Account views
class AccountList(ListView):
    model = Account
    template_name = 'account_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) |
                Q(last_name__icontains=search_query) |
                Q(iban__icontains=search_query)
            )
        return queryset

class AccountDetailView(DetailView):
    model = Account

class AccountCreateView(LoginRequiredMixin, CreateView):
    model = Account
    fields = ['first_name', 'last_name', 'iban', 'balance']
    template_name = 'main/account_form.html'
    success_url = reverse_lazy('account_list')

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    model = Account
    fields = ['first_name', 'last_name', 'iban', 'balance']
    template_name = 'main/account_form.html'
    def get_success_url(self):
        return reverse_lazy('account_detail', kwargs={'pk': self.object.pk})

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    model = Account
    template_name = 'main/account_confirm_delete.html'
    success_url = reverse_lazy('account_list')

# Category Views
class CategoryList(ListView):
    model = Category
    template_name = 'category_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')

        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) |
                Q(description__icontains=search_query)
            )
        return queryset

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(CreateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryUpdateView(UpdateView):
    model = Category
    fields = ['name', 'description']
    template_name = 'main/category_form.html'
    success_url = reverse_lazy('category_list')

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = 'main/category_confirm_delete.html'
    success_url = reverse_lazy('category_list')

# Transaction Views
class TransactionList(ListView):
    model = Transaction
    template_name = 'transaction_list.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        income_filter = self.request.GET.get('income')
        search_query = self.request.GET.get('q')

        if income_filter == 'true':
            queryset = queryset.filter(is_income=True)
        elif income_filter == 'false':
            queryset = queryset.filter(is_income=False)

        if search_query:
            queryset = queryset.filter(
                Q(description__icontains=search_query) |
                Q(category__name__icontains=search_query)
            )

        return queryset

class TransactionDetailView(DetailView):
    model = Transaction

class TransactionCreateView(CreateView):
    model = Transaction
    fields = ['account', 'category', 'amount', 'description', 'is_income']
    template_name = 'main/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionUpdateView(UpdateView):
    model = Transaction
    fields = ['account', 'category', 'amount', 'description', 'is_income']
    template_name = 'main/transaction_form.html'
    success_url = reverse_lazy('transaction_list')

class TransactionDeleteView(DeleteView):
    model = Transaction
    template_name = 'main/transaction_confirm_delete.html'
    success_url = reverse_lazy('transaction_list')
