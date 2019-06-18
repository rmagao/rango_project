from django.urls import path
from rango import views

app_name = 'rango'
urlpatterns = [
    path('rango/', views.index, name='index'),
    path('rango/about/', views.about, name='about'),
    path('rango/category/<slug:category_name_slug>/', views.show_category, name='show_category'),
    path('rango/add_category/', views.add_category, name='add_category'),
    path('rango/category/<category_name_slug>/add_page/', views.add_page, name='add_page')
]
