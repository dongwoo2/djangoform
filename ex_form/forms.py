from django import forms
from django.core.validators import MaxLengthValidator , MinLengthValidator # 자주 사용되고 보편적인 유효성 검증기가 들어있다

def my_validator(value):
    if value < 0:
        raise forms.ValidationError('나이는 음수를 사용할 수 없음')
    return value

def my_validator2(value):
    if '!' in value:
        raise forms.ValidationError('이름에 !를 사용할 수 없음')
    return value

class PersonForm(forms.Form):
    name = forms.CharField(
        label='이름',
        max_length=20,
        required=True,
        validators=[
            MaxLengthValidator(limit_value=20),
            MinLengthValidator(limit_value=4),
            my_validator2,
            ]
    )
    age = forms.IntegerField(
        label='나이',   
        required=True,
        validators=[
            my_validator,
        ]
    )
    
    #def clean_필드명  파라미터 검증에 사용되는 메서드
    def clean_age(self):
        age = self.cleaned_data.get('age', 0)
        if age > 150:
            raise forms.ValidationError('값이 범위를 벗어남')
        return age # 반드시 값을 반환해야함
    
from .models import Person

class PersonModelForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['name', 'age']