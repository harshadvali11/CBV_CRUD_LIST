from django.shortcuts import render

# Create your views here.
from app.models import *
from django.views.generic import ListView,TemplateView,DetailView

class Home(TemplateView):
    template_name='app/home.html'

class SchoolList(ListView):
    model=School
    context_object_name='schools'
    #template_name='app/school_list.html'
    #queryset=School.objects.filter(name='Jspiders')
    ordering=['name']

class SchoolDetail(DetailView):
    model=School
    context_object_name='sc'












