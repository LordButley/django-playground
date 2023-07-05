from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from djdatepicker.forms import DataPickerModelForm, DatePickerForm
from djdatepicker.models import Datepicked
from django.contrib.admin.widgets import AdminDateWidget

# Create your views here.

def datepickerindex(request):
    
    form = DatePickerForm()
    formb = DataPickerModelForm()
    if request.method == "POST":
        print(request.POST)
        date = DatePickerForm(request.POST).data["date"]
        # date_picked = Datepicked(date=date)
        # date_picked.save()

        date_picked = Datepicked.objects.create(date=date)

    context = {
        "form": form,
        "formb": formb,
    }

    return render(request, "djdatepicker/index.html", context)


class DatePickerClassView(CreateView):
    
    model = Datepicked
    form_class = DataPickerModelForm
    template_name = "djdatepicker/indexclass.html"
    success_url = reverse_lazy("dpcreateclass")
    
class DatePickerWidgetView(CreateView):
    template_name = "djdatepicker/indexclass.html"
    model = Datepicked
    fields = ['date']
    success_url = reverse_lazy("dpcreatewidget")


    def get_form(self, form_class=None):
        form = super(DatePickerWidgetView, self).get_form(form_class)
        form.fields['date'].widget = AdminDateWidget(attrs={'type': 'date'})
        return form




