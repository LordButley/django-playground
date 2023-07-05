from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class DatePickerForm(forms.Form):
    """
    Last Active Date Form
    """
    date = forms.DateField(widget=DateInput)