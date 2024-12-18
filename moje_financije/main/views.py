from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.views.generic import ListView
from main.models import *
from django.views.generic.detail import DetailView

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
    
class CategoryList(ListView):
    model = Category
    
class TransactionList(ListView):
    model = Transaction
    
class TransactionDetailView(DetailView):
    model =Transaction