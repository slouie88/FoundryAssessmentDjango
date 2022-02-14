from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('employees/search', views.employee_client_search, name='employees_form'),
    path('employees/<id>', views.render_page, name='employees_by_id'),
    path('employees', views.render_page, name='employees'),
    path('clients/<id>', views.render_page, name='clients_by_id'),
    path('clients', views.render_page, name='clients'),
    path('engagements/<id>', views.render_page, name='engagements_by_id'),
    path('engagements', views.render_page, name='engagements'),
]