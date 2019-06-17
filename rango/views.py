from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
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
    page_list = Page.objects.order_by('-views')[:5]
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!',
                    'categories': category_list,
                    'pages': page_list,}
    return render(request, 'rango/index.html', context_dict)

def about(request):
    context_dict = {'boldmessage' : 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/about.html', context=context_dict)

def rango(request):
    return HttpResponse('<h1>Rango</h1>')

def login(request):
    return HttpResponse('Login Page')

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['category'] = None
        context_dict['pages'] = None
    return render(request, 'rango/category.html', context=context_dict)

def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database
            cat = form.save(commit=True)
            # New that the category is saved
            # We could give a confirmation boldmessage
            # But since the most recent category added is on the index Page
            # Then we can direct the ussesr back to the index page.
            return index(request)
        else:
            # The supplied form contained errors
            # Just print them to the terminal
            print(form.errors)

    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'rango/add_category.html', {'form': form})

def add_page(request, category_name_slug):
    try:
        category = Category.objects.get(slug=category_name_slug)
    except Category.DoesNotExist:
        category = None

    form = PageForm()

    if request.method == 'POST':
        form = PageForm(request.POST)

        if form.is_valid():
            page = form.save(commit=False)
            page.category = category
            page.views = 0
            page.save()
            return show_category(request, category_name_slug)
        else:
            print(form.errors)

    context_dict = {'form': form, 'category': category}
    return render(request, 'rango/add_page.html', context_dict)
