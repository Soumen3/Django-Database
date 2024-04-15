from django import forms

class StudentRegistration(forms.Form):
    user_Name=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())
    about=forms.CharField(widget=forms.Textarea)
    can_drive=forms.CharField(widget=forms.CheckboxInput)
    photo=forms.CharField(widget=forms.FileInput)
    hobbey=forms.CharField(widget=forms.TextInput(attrs={'class=':'css1', 'id':'unique'}))