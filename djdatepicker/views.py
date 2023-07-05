from django.shortcuts import render

from djdatepicker.forms import DatePickerForm
from djdatepicker.models import Datepicked

# Create your views here.

def datepickerindex(request):
    
    form = DatePickerForm()
    if request.method == "POST":
        date = DatePickerForm(request.POST).data["date"]
        # date_picked = Datepicked(date=date)
        # date_picked.save()

        date_picked = Datepicked.objects.create(date=date)


    return render(request, "djdatepicker/index.html", {"form":form})