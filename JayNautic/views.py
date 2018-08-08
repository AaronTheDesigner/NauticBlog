from django.http import HttpResponse
from django.shortcuts import render
from articles.models import Article, Cover, Novel, Event, Podcast

def homepage(request):
  #return HttpResponse('homepage')
  covers = Cover.objects.all()
  novels = Novel.objects.all()
  events = Event.objects.all()
  

  return render(request, 'homepage.html', {'covers': covers, 'novels': novels, 'events': events})

def podcast(request):
  #return HttpResponse('about')
  podcasts = Podcast.objects.all()
  return render(request, 'podcast.html', {'podcasts': podcasts})