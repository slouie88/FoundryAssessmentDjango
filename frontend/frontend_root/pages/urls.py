from unicodedata import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employees', views.render_page, name='employees'),
    path('employees/<id>', views.render_page, name='employees_by_id'),
    path('clients', views.render_page, name='clients'),
    path('clients/<id>', views.render_page, name='clients_by_id'),
    path('engagements', views.render_page, name='engagements'),
    path('engagements/<id>', views.render_page, name='engagements_by_id')
]