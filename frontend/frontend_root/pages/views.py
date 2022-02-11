from django.shortcuts import render

# Create your views here.
"""
Render the home page of the website.
"""
def index(request):
    return render(request, 'base.html')