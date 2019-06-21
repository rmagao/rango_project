from django.urls import path
from rango import views
from rango.views import AboutView, AddCategoryView, ProfileView

app_name = 'rango'
urlpatterns = [
    path('rango/', views.index, name='index'),
    path('rango/about/', AboutView.as_view(), name='about'),
    path('rango/category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('rango/add_category/', AddCategoryView.as_view(), name='add_category'),
    path('rango/category/<category_name_slug>/add_page/', views.add_page, name='add_page'),
    #path('rango/search/', views.search, name='search'),
    path('rango/goto/', views.goto_url, name='goto'),
    path('rango/register_profile/', views.register_profile, name='register_profile'),
    path('rango/profile/<username>/', ProfileView.as_view(), name='profile'),
    path('rango/profiles/', views.list_profiles, name='list_profiles'),
    path('rango/like/', views.like_category, name='like_category'),
    path('rango/suggest/', views.suggest_category, name='suggest_category'),
    path('rango/add/', views.auto_add_page, name='auto_add_page'),
]
