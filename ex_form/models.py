from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator
# Create your models here.
def validate_name_length(value):
    print('name 유효성 검증')
    if len(value) < 4:
        raise ValidationError('길이 오류')
    return value
    
def validate_age_scope(value):
    print('age 유효성 검증')
    if not 0 < value < 150:
        raise ValidationError('나이 범위 오류')
    return value

class Person(models.Model):
    name = models.CharField(
        max_length=20,
        null=False,
        validators=[
            validate_name_length,
            MaxLengthValidator(
                limit_value=20,
                message='최대 길이 오류'),
        ])
    age = models.IntegerField(
        null=False,
        validators=[
            validate_age_scope,
        ])
    


    def __str__(self):
        return f'Person[id={self.id}, name={self.name}, age={self.age}]'