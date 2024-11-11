from django import forms
from django.core import validators

class Investor(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5,'please type more than 5')])
    email = forms.CharField(validators=[validators.MinLengthValidator(10,'please type more than 10')])