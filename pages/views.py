from django.shortcuts import render
from django.http import HttpResponse

from news.models import NewsDetails
# Create your views here.

def index(request):
    keys = NewsDetails.objects.order_by('-published_date').filter(is_published=True)[:3]

    context = {
        'keys': keys
    }

    return render(request, 'pages/index.html', context)

def courses(request):
    return render(request, 'pages/courses.html')

def it_and_tech(request):
    return render(request, 'pages/it_and_tech.html')

def others(request):
    return render(request, 'pages/others.html')