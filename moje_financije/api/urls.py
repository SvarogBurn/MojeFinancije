from django.urls import path
from api import views

urlpatterns = [
    path('v1/accounts/', views.AccountList.as_view()),
    path('v1/accounts/<int:pk>/', views.AccountDetailView.as_view()),
]