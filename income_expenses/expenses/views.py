from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Expense
from .forms import ExpenseForm


def expenses_list(request):
    """Expenses list."""
    template = 'expenses/expenses_list.html'
    expenses = Expense.objects.all()
    context = {
        'expenses': expenses
    }
    return render(request, template, context)


class AddExpenseView(CreateView):
    """Add expense."""
    template_name = 'expenses/expenses_form.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses:expenses_list')


class UpdateExpenseView(UpdateView):
    """Update expense."""
    model = Expense
    template_name = 'expenses/expenses_form.html'
    form_class = ExpenseForm
    success_url = reverse_lazy('expenses:expenses_list')


class DeleteExpenseView(DeleteView):
    """Delete expense."""
    model = Expense
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('expenses:expenses_list')
