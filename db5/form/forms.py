from django import forms

class registration(forms.Form):
    name=forms.CharField(initial="Soumen",)
    email=forms.EmailField(help_text='Only 30 characters')

