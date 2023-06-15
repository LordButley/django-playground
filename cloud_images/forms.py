from django import forms
from .models import CloudImage

class CloudImageForm(forms.ModelForm):

    class Meta:
        model = CloudImage
        fields = ['image']