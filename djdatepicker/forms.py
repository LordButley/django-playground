from django import forms

from djdatepicker.models import Datepicked

class DateInput(forms.DateInput):
    input_type = 'date'

class DatePickerForm(forms.Form):
    """
    Last Active Date Form
    """
    date = forms.DateField(widget=DateInput)

class DataPickerModelForm(forms.ModelForm):

    date = forms.DateField(widget=DateInput)

    class Meta:
        model = Datepicked
        fields = '__all__'
