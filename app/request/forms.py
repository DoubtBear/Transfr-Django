from django import forms
from .models import Post
import datetime
from django.utils.translation import gettext_lazy as _

DESTINATION_LOCATIONS = [
    ('RedMed','Red Med'),
    ('OOSM','Oxford Bone Doctor'),
    ('BSMH','Baptist Street Memorial Hosptial')
]

class RiderRequestForm(forms.ModelForm):
    riderLocation = forms.CharField(label='Pickup Location')
    destination = forms.CharField(initial="------",label='Select your destination: ', widget=forms.Select(choices=DESTINATION_LOCATIONS))
    date = forms.DateTimeField(label='Enter the date of ride, Year-Month-Day Hour:Min:Sec',initial= datetime.date.today, widget=forms.DateTimeInput())
    addSupport = forms.CharField(label='List any additional information we should know: ', max_length=200, required=False)
    tip = forms.DecimalField(label='Optional Tip: $', required=False)

    class Meta:
        model = Post
        fields = ['riderLocation', 'destination','date','addSupport','tip']
      