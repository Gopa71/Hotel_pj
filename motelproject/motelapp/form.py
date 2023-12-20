from django import forms
from .models import Hotel

class Motelupdate(forms.ModelForm):

    class Meta:
        model=Hotel
        fields='__all__'