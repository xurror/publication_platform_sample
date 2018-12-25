from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.courses, name='courses'),
    path('it_and_tech/', views.it_and_tech, name='it_and_tech'),
    path('others/', views.others, name='others'),
]