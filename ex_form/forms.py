from django import forms

class PersonForm(forms.Form):
    name = forms.CharField(
        label='이름',
        max_length=20,
        required=True,
    )
    age = forms.IntegerField(
        label='나이',   
        required=True,
    )