from asyncio.windows_events import NULL
from django.shortcuts import render
import requests

# Create your views here.
"""
Render the home page of the website.
"""
def index(request):
    return render(request, 'base.html')


"""
Render the employees page, displaying the list of employees.
"""
def get_employees(request):
    employees = requests.get('http://localhost:3000/employees')
    
    context = {"employees": employees.json()}
    
    return render(request, 'pages/employees.html', context)
