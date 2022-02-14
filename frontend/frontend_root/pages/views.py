import re
from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect

from datetime import datetime
from .forms import EmployeeClientForm
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
def render_page(request, id=''):
    path = request.path
    content = requests.get('http://localhost:3000' + path).json()
    last_updated = datetime.now()
    title = ''
    html_page = ''

    # Determine which template to render.
    if 'employees' in path:
        html_page = 'pages/employees.html'
        title = 'Employees'
    elif 'clients' in path:
        html_page = 'pages/clients.html'
        title = 'Clients'
    elif 'engagements' in path:
        html_page = 'pages/engagements.html'
        title = 'Engagements'

    if id != '':
        content = [content]

    # Context to render alongside the appropriate template.
    context = {
        "content": content,
        "last_updated": last_updated,
        "pageTitle": title
    }

    return render(request, html_page, context)

"""
Renders the employees/clientshh page according to the user's search.
"""
def employee_client_search(request):
    if request.method == "POST":
        form = EmployeeClientForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            path = 'employees'
            
            if 'clients' in request.path:
                path = 'clients'

            if cd['id'] != '':
                try:
                    return HttpResponseRedirect(cd['id'])
                except:
                    raise Http404("Id does not exist")
            elif cd['name'] != '':
                content = requests.get('http://localhost:3000' + path).json()
                for entity in content:
                    if entity.name != cd['name']:
                        content.remove(entity)
                return render(request, 'pages/' + path + '.html')
    else:
        form = EmployeeClientForm()

    return render(request, 'pages/employeeclientsearch.html', {'form': form, 'pageTitle':'Employee/Client Search'})


