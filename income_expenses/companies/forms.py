from django import forms

from .models import Company, CompanyType, Requisites


class DateInput(forms.DateInput):
    """Custom field date."""
    input_type = 'date'
    input_formats = ['%Y-%m-%d']


class CompanyForm(forms.ModelForm):
    """Form for Company."""

    class Meta:
        model = Company
        exclude = ('requisites',)


class RequisitesForm(forms.ModelForm):
    """Form for Requisites."""

    class Meta:
        model = Requisites
        fields = '__all__'
        widgets = {
            'date_reg': DateInput(format='%Y-%m-%d'),
        }
