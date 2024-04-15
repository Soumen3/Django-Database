from django import forms 


class StudentRegistration(forms.Form):
    name=forms.CharField()
    Email=forms.EmailField()
    mobile=forms.IntegerField()
    key=forms.IntegerField(widget=forms.HiddenInput())


class StudentRegistration2(forms.Form):
    name=forms.CharField(label='Your Name', label_suffix='->', initial='Soumen Samanta', required=False, disabled=True)
    Email=forms.EmailField(label='Your E-mail', label_suffix='->', initial='abc@gmail.com',)
    mobile=forms.IntegerField(label='Your ph no.', label_suffix='->', initial='9876543210',)
    key=forms.IntegerField(widget=forms.HiddenInput())