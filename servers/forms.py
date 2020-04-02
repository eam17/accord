from django import forms

class ServerForm(forms.Form):
    display_name = forms.CharField(label="Server name", max_length=100)
