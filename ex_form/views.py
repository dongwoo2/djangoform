from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Person

def exam01(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        print('요청 처리:', name, age)
        Person(name=name, age=age).save() #모델에 저장
        return HttpResponse('처리 완료')
    else:
        return render(request, 'ex_form/exam01_form.html')
    
from .forms import PersonForm

def exam02(request):
    if request.method == 'POST':
        personForm = PersonForm(request.POST)
        if personForm.is_valid(): # 유효성 검증
            name = personForm.cleaned_data['name']
            age = personForm.cleaned_data['age']
            Person(name=name, age=age).save() #모델에 저장
            return HttpResponse('처리 완료')
        else:
            return render(
                request,
                'ex_form/exam02_form.html',
                {'form': personForm}
            )
    else:
        form = PersonForm()
        print(form)
        return render(
            request, 
            'ex_form/exam02_form.html',
            {'form':form}     
        )
    
from .forms import PersonModelForm

def exam03(request):
    if request.method == 'POST':
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save
            return HttpResponse('처리 완료')
    else:
        form = PersonModelForm()

    return render(
        request,
        'ex_form/exam03_form.html',
        {'form': form}
    )
    
def index(request):
    return render(request, 'ex_form/index.html')
