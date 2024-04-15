from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showForm(request):
    fm=StudentRegistration()

    return render (request, 'enroll/forms.html', {'form':fm})