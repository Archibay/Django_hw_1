from catalog.models import Person

from django import forms
from django.forms import ModelForm


class Triangle(forms.Form):
    cathetus_1 = forms.FloatField(min_value=1)
    cathetus_2 = forms.FloatField(min_value=1)


class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
