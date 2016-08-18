from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse(" Rango says: Hello world! <br/> <a href='/rango/about'>About</a>")

def about(request):
    return render(request, 'rango/about.html', {})
# Create your views here.
