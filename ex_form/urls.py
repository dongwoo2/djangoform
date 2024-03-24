from django.urls import path
from . import views

app_name ='ex_form'

urlpatterns = [
    path('exam01/', views.exam01, name='exam01'),
    path('exam02/', views.exam02, name='exam02'),
    path('exam03/', views.exam03, name='exam03'),
]
