from asyncio.windows_events import NULL
import re
from django.shortcuts import render

from datetime import datetime
import requests

"""
Render the home page of the website.
"""
def index(request):
    return render(request, 'base.html')


### GET Requests for employees, clients and engagements ###

"""
Render either the employees, clients or engagements page.
"""
def render_page(request):
    content = requests.get('http://localhost:3000' + request.path)
    last_updated = datetime.now()
    title = ''
    html_page = ''

    if 'employees' in request.path:
        html_page = 'pages/employees.html'
        title = 'Employees'
    elif 'clients' in request.path:
        html_page = 'pages/clients.html'
        title = 'Clients'
    elif 'engagements' in request.path:
        html_page = 'pages/engagements.html'
        title = 'Engagements'

    context = {
        "content": content.json(),
        "last_updated": last_updated,
        "pageTitle": title
    }

    return render(request, html_page, context)


