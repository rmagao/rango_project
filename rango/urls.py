from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', views.rango, name='rango'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('category/<slug:category_name_slug>/', views.show_category, name='show_category')
]
