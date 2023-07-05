from django.db import models

# Create your models here.

class Datepicked(models.Model):
    
    date = models.DateField()
    