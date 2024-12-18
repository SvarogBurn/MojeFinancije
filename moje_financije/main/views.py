from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from main.models import *
from django.views.generic.detail import DetailView
from django.db.models import Q

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



class AccountList(ListView):
    model = Account
    template_name = 'account_list.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')  # Get the search query

        if search_query:
            queryset = queryset.filter(
                Q(first_name__icontains=search_query) | 
                Q(last_name__icontains=search_query) |   
                Q(iban__icontains=search_query)  
            )       
        return queryset
    
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
    model =Transaction
    #template_name = 'transaction_detail.html'
    
    
class AccountDetailView(DetailView):
    model =Account
