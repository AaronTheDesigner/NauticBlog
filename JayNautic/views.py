from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
  #return HttpResponse('homepage')
  return render(request, 'homepage.html')

def podcast(request):
  #return HttpResponse('about')
  return render(request, 'podcast.html')