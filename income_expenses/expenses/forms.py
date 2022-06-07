from django import forms

from .models import Expense
from core.forms import DateInput


class ExpenseForm(forms.ModelForm):
    """Form for Expenses."""

    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
        }
