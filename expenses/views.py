from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Expense
from django.db.models import Sum

# Create your views here.

class ExpenseListView(ListView):
    model = Expense
    template_name = 'expense_list.html'
    context_object_name = 'expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['total_expense']= (
            Expense.objects.aggregate(total=Sum('amount'))
            ['total'] or 0
        )

        return context


class ExpenseCreateView(CreateView):
    model = Expense
    fields = ['title', 'amount', 'category','description', 'date']
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense_list')


class ExpenseUpdateView(UpdateView):
    model = Expense
    fields = ['title', 'amount', 'category', 'description', 'date']
    template_name = 'expense_form.html'
    success_url = reverse_lazy('expense_list')


class ExpenseDeleteView(DeleteView):
    model = Expense
    template_name = 'expense_confirm_delete.html'
    success_url = reverse_lazy('expense_list')