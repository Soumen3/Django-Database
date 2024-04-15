from django.shortcuts import render
from .forms import StudentRegistration
from .forms import StudentRegistration2

# Create your views here.
def showFormData(request):
    fm=StudentRegistration()
    fm2=StudentRegistration2()
    return render(request, 'form.html', {'form':fm, 'form2':fm2})