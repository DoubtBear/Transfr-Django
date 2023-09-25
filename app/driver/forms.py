from django import forms
from .models import DriverPayment

class CloseRideForm(forms.Form):
    
    milage = forms.DecimalField(decimal_places=2, label="Enter milage in miles")

    class Meta:
        
        fields = ('milage',)
