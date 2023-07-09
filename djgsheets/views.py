from django.shortcuts import render

# Create your views here.

def gsheetsindex(request):


    return render(request, "djgsheets/index.html")