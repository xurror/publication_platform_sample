from django.shortcuts import render
from django.http import HttpResponse
from . models import NewsDetails
# Create your views here.

def courses(request):
    
    keys = NewsDetails.objects.all()
    
    context = {
        'keys' : keys
    }
    return render(request, 'news/courses.html', context)

def news_details(request, news_details_id):
    return render(request, 'news/news_details.html')

def search(request):
    return render(request, 'newss/search.html')