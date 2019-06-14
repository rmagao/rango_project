from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
# Create your views here.
def index(request):
    #context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    #return render(request, 'rango/index.html', context=context_dict)

    # Query the database for a list of ALL categories currently stored.
    # Order the categories by no. likes in descending order.
    # Retrieve the top 5 only - or all if less than 5.
    # Place the list in our context_dict dictionary
    # that will be passed to the template engine.

    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'about/about.html', context=context_dict)

def rango(request):
    return HttpResponse('<h1>Rango</h1>')

def login(request):
    return HttpResponse('Login Page')

def show_category(request, category_name_slug):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)
