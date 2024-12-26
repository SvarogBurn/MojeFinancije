from django.urls import path
from .views import *
urlpatterns = [    
    path('', index, name='index'),
    path('register/', register, name='register'),
    
    path('accounts/', AccountList.as_view(), name='account_list'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/create/', AccountCreateView.as_view(), name='account_create'),
    path('accounts/<int:pk>/', AccountDetailView.as_view(), name='account_detail'),
    path('accounts/<int:pk>/update/', AccountUpdateView.as_view(), name='account_update'),
    path('accounts/<int:pk>/delete/', AccountDeleteView.as_view(), name='account_delete'),

    path('categories/', CategoryList.as_view(), name='category_list'),
    path('categories/create/', CategoryCreateView.as_view(), name='category_create'),
    path('categories/<int:pk>/update/', CategoryUpdateView.as_view(), name='category_update'),
    path('categories/<int:pk>/delete/', CategoryDeleteView.as_view(), name='category_delete'),

    path('transactions/', TransactionList.as_view(), name='transaction_list'),
    path('transactions/<int:pk>/', TransactionDetailView.as_view(), name='transaction_detail'),
    path('transactions/create/', TransactionCreateView.as_view(), name='transaction_create'),
    path('transactions/<int:pk>/update/', TransactionUpdateView.as_view(), name='transaction_update'),
    path('transactions/<int:pk>/delete/', TransactionDeleteView.as_view(), name='transaction_delete'),
]

    