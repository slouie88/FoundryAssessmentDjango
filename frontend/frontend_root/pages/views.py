from asyncio.windows_events import NULL
from django.shortcuts import render

from datetime import datetime
import requests

# Create your views here.
"""
Render the home page of the website.
"""
def index(request):
    return render(request, 'base.html')


### GET Requests for employees, clients and engagements ###

"""
Render the employees page, displaying the list of employees.
"""
def get_employees(request):
    employees = requests.get('http://localhost:3000/employees')
    last_updated = datetime.now()
    context = {
        "employees": employees.json(),
        "last_updated": last_updated,
        "pageTitle": "Employees"
    }
    
    return render(request, 'pages/employees.html', context)

"""
Render the clients page, displaying the list of clients.
"""
def get_clients(request):
    clients = requests.get('http://localhost:3000/clients')
    last_updated = datetime.now()
    context = {
        "clients": clients.json(),
        "last_updated": last_updated,
        "pageTitle": "Clients"
    }
    
    return render(request, 'pages/clients.html', context)

"""
Render the engagements page, displaying the list of engagements.
"""
def get_engagements(request):
    engagements = requests.get('http://localhost:3000/engagements')
    last_updated = datetime.now()
    context = {
        "engagements": engagements.json(),
        "last_updated": last_updated,
        "pageTitle": "Engagements"
    }

    return render(request, 'pages/engagements.html', context)
