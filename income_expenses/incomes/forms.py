from django import forms

from .models import Income
from core.forms import DateInput


class IncomeForm(forms.ModelForm):
    """Form for Incomes."""

    class Meta:
        model = Income
        fields = '__all__'
        widgets = {
            'date': DateInput(format='%Y-%m-%d'),
        }
