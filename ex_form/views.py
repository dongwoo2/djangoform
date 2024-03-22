from django.shortcuts import render

# Create your views here.

def exam01(request):
    if request.method == 'POST':
        print('exam01')
    else:
        return render(request, 'ex_form/exam01_form.html')
    
from .forms import PersonForm

def exam02(request):
    if request.method == 'POST':
        pass
    else:
        form = PersonForm()
        return render(
            request, 
            'ex_form/exam02_form.html',
            {'form':form}     
        )