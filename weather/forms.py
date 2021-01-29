from django import forms

class searchForm(forms.Form):
    location=forms.CharField(max_length=500)