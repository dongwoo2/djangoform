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

from django.views.generic import View
from django.shortcuts import redirect, reverse

class MyView1(View):
    
    def get(self, request):
        form = PersonModelForm()
        return render(request, 'ex_form/exam04_form.html', {'form':form})
    
    def post(self, request):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ex_form:index'))
        
        return render(request, 'ex_form/exam04_form.html', {'form':form})
    
    
class MyView2(View):
    form_class = PersonModelForm
    initial = {
        'name' : '이름',
        'age' : 0
    }
    template_name = 'ex_form/exam04_form.html'
    
    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form':form})
    
    def post(self, request):
        form = PersonModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse('ex_form:index'))
        
        return render(request, self.template_name, {'form':form})
    
from django.views.generic import FormView # FormView는 폼까지만 보여줌 폼이 정상적인지까지만 확인해서 거기까지만 진행될 수 있게 함

class MyView3(FormView): # 0.formview를 상속해서 클래스형 뷰를 정의하면
    form_class = PersonModelForm # 1.폼으로 사용할 클래스 정의
    template_name = 'ex_form/exam04_form.html' # 2.그 때 사용될 템플릿 이름을 정의
    success_url = '/ex/'  # 3. 해당 폼을 통해서 요청에 post로 들어왔을 때  # 5. 로직이 잘 끝나면 브라우저에다가 여기로 다시 요청함 redirect로 사용될 경로를 지정 form이 유효하지 않다면 invalid 사용
    
    def form_valid(self, form): # form_valid는 오버라이딩을 하고 있는 상황
        print('데이터가 유효하면') # 4. 데이터가 유효하면 어떤 작업을 할 것인지 정의
        m = Person(**form.cleaned_data)
        m.save()
        
        return super().form_valid(form) # 내가 원하는 기능을 다 만든 후 에는 부모가 갖고있는 동일한 함수를 매개변수를 그대로 전달해줘서 호출해주고 리턴해야한다