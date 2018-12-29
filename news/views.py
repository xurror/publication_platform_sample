from django.shortcuts import render
from django.db.models import Q
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
    search_list = NewsDetails.objects.order_by('-published_date')
    
    # Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            search_list = search_list.filter(Q(title__icontains=keywords) | 
            Q(description__icontains=keywords))
            
    
    context = {
        'keys' : search_list,
        'values' : request.GET
    }
    return render(request, 'news/search.html', context)