from django import forms

class math_forum(forms.Form):
    title = forms.CharField(label = "Title", required = True)
    description = forms.CharField(label = "Description", requred = True)