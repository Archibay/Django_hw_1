from django import forms
from django.forms import ModelForm
from catalog.models import Person


class Triangle(forms.Form):
    cathetus_1 = forms.FloatField(min_value=1)
    cathetus_2 = forms.FloatField(min_value=1)


class Person1(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email']
