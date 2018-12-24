from django import forms

class NavSearch(forms.Form):
    plate_number = forms.CharField(max_length=20)
