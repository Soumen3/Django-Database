from django import forms

class StudentRegistration(forms.Form):
    name=forms.CharField()
    Email=forms.EmailField(required=False)
    password=forms.CharField(widget=forms.PasswordInput)