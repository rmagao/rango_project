from django.urls import path
from rango import views

urlpatterns = [
    path('', views.index, name='index'),
    path('rango/', views.rango, name='rango'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
]
