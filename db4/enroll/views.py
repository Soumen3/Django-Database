from django.shortcuts import render
from .forms import StudentRegistration
# Create your views here.

def showFormData(request):
    fm=StudentRegistration(auto_id=True, label_suffix='- ', initial={
        'name':'soumen'
    })
    fm.order_fields(field_order=['last_name','name','email'])

    return render(request, 'enroll/userRegistration.html', {'form':fm})
