from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse('<h1><em>About Page</em></h1>')

def rango(request):
    return HttpResponse('<h1>Rango</h1>')

def login(request):
    return HttpResponse('Login Page')
