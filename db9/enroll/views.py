from django.shortcuts import render, redirect
from .forms import StudentRegistration
from django.http import HttpResponseRedirect
# Create your views here.


def showForm(request):
    if request.method == 'POST':
        fm=StudentRegistration(request.POST)
        if fm.is_valid():
            print('Form Validation')
            print('Name:',fm.cleaned_data['name'])
            print('Email:',fm.cleaned_data['email'])
        return HttpResponseRedirect('/success/')
        # return redirect('success')
    else:
        fm=StudentRegistration()
        print('This is get request')
    return render(request, 'enroll/registration.html',{'form':fm})


def success(request):
    return render(request, 'enroll/success.html')
