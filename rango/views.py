from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('<h1>Rango says hey there partner!</h1>')

def about(request):
    return HttpResponse('<h1><em>About Page</em></h1>')

def rango(request):
    return HttpResponse('<h1>Rango</h1>')

def login(request):
    return HttpResponse('Login Page')
