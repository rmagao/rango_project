from django.shortcuts import render
from django.http import HttpResponse
from rango.models import Category, Page
from rango.forms import CategoryForm, PageForm
from datetime import datetime

# Create your views here.
def visitor_cookie_handler(request, response):
    # Get the number of visits to the site.
    # We use the COOKIES.get() function to obtain the visits cokie.
    # If the cookie exists, the value returned is casted to an integer
    # If the cookie doesnt exist, then the default value of 1 is used.
    visits = int(request.COOKIES.get('visits', '1'))

    last_visit_cookie = request.COOKIES.get('last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],
                                        '%Y-%m-%d %H:%M:%S')

    # If its been more that a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        response.set_cookie('last_visit', str(datetime.now()))
    else:
        # Set the last visit cookie
        response.set_cookie('last_visit', last_visit_cookie)

    #Update/set the visits COOKIE
    response.set_cookie('visits', visits)

def index(request):
    request.session.set_test_cookie()

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

    # Obtain our Response object early so we can add cookie information.
    response = render(request, 'rango/index.html', context_dict)

    # Call the helper function to handle the COOKIES
    visitor_cookie_handler(request, response)

    # Return response back to the user, updating any cookies that need changed.
    return response

def about(request):
    print('TEST COOKIE WORKED!')
    request.session.delete_test_cookie()
    context_dict = {}
    return render(request, 'rango/about.html', context=context_dict)

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
