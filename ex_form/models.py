from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=20, null=False)
    age = models.IntegerField(null=False)
    
    def __str__(self):
        return f'Person[name={self.name}, age={self.age}]'