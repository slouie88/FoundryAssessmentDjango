from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employees', views.render_page, name='employees'),
    path('clients', views.render_page, name='clients'),
    path('engagements', views.render_page, name='engagements')
]