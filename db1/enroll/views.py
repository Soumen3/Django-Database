from django.shortcuts import render
from enroll.models import Students
# Create your views here.


def studentinfo(request):
    stud = Students.objects.all()
    return render(request, 'enroll/studetails.html', {'stu': stud})
