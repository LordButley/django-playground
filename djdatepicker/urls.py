from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.datepickerindex, name="dpindex"),
    path("datepickerclassview/", views.DatePickerClassView.as_view(), name="dpcreateclass"),
    path("datepickerclasswidget/", views.DatePickerWidgetView.as_view(), name="dpcreatewidget"),

]
