from django import forms


class Triangle(forms.Form):
    cathetus_1 = forms.FloatField(min_value=1)
    cathetus_2 = forms.FloatField(min_value=1)
