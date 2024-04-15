from django import forms 


class StudentRegistration(forms.Form):
    name=forms.CharField()
    last_name=forms.CharField()
    email=forms.EmailField()