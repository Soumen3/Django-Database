from django.shortcuts import render
from .forms import registration

# Create your views here.
def showForm(request):
    fm=registration()
    return render(request, 'form/form.html', {'form':fm})
