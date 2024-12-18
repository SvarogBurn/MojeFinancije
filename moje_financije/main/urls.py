from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('account/', views.AccountList.as_view(), name='account'),
    path('category/', views.CategoryList.as_view(), name='category'),
    path('transaction/', views.TransactionList.as_view(), name='transaction'),
    path('<pk>/', views.TransactionDetailView.as_view(), name='transaction_detail'),
]