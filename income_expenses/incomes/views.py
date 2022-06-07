from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, UpdateView

from .models import Income
from .forms import IncomeForm


def incomes_list(request):
    """Incomes list."""
    template = 'incomes/incomes_list.html'
    incomes = Income.objects.all()
    context = {
        'incomes': incomes
    }
    return render(request, template, context)


class AddIncomeView(CreateView):
    """Add income."""
    template_name = 'incomes/incomes_form.html'
    form_class = IncomeForm
    success_url = reverse_lazy('incomes:incomes_list')


class UpdateIncomeView(UpdateView):
    """Update income."""
    model = Income
    template_name = 'incomes/incomes_form.html'
    form_class = IncomeForm
    success_url = reverse_lazy('incomes:incomes_list')


class DeleteIncomeView(DeleteView):
    """Delete income."""
    model = Income
    template_name = 'confirm_delete.html'
    success_url = reverse_lazy('incomes:incomes_list')
