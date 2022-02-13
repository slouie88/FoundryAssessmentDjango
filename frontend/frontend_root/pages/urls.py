from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employees', views.get_employees, name='employees')
]