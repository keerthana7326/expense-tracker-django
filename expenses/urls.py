from django.contrib import admin
from django.urls import path
from .views import ExpenseListView, ExpenseCreateView, ExpenseUpdateView, ExpenseDeleteView

urlpatterns = [
    path('', ExpenseListView.as_view(), name='expense_list'),
    path('add/', ExpenseCreateView.as_view(), name='expense_add'),
    path('edit/<int:pk>/', ExpenseUpdateView.as_view(), name='expense_edit'),
    path('delete/<int:pk>/', ExpenseDeleteView.as_view(), name='expense_delete'),
]