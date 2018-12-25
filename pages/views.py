from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'pages/index.html')

def courses(request):
    return render(request, 'pages/courses.html')

def it_and_tech(request):
    return render(request, 'pages/it_and_tech.html')

def others(request):
    return render(request, 'pages/others.html')