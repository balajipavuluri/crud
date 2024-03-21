from .models import Contactinfo
from django import forms

class Contactform(forms.Form):
 
    """Contactform definition."""
    class Meta: 

        model=Contactinfo()
        fields=['name','number']


    # TODO: Define form fields here
