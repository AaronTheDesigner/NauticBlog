from django.shortcuts import render
from .models import Article, Cover, Novel, Event, Podcast, Novella, Short
from django.http import HttpResponse

# Create your views here.
def article_list(request):
  articles = Article.objects.all().order_by('-date')
  return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
  #return HttpResponse(slug)
  article = Article.objects.get(slug=slug)
  return render(request, 'articles/article_detail.html', {'article': article})

def homepage(request):
  #return HttpResponse('homepage')
  covers = Cover.objects.all()
  novels = Novel.objects.all()
  events = Event.objects.all()
  novellas = Novella.objects.all()
  shorts = Short.objects.all()
  

  return render(request, 'homepage.html', {'covers': covers, 'novels': novels, 'events': events, 'novellas': novellas, 'shorts': shorts})

def podcast(request):
  #return HttpResponse('about')
  podcasts = Podcast.objects.all()
  return render(request, 'podcast.html', {'podcasts': podcasts})
