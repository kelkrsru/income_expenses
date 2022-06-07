from django import forms


class DateInput(forms.DateInput):
    """Custom field date."""
    input_type = 'date'
    input_formats = ['%Y-%m-%d']
