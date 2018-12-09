from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
#Fo Blog
class Article(models.Model):
  title = models.CharField(max_length=100)
  slug = models.SlugField()
  body = RichTextField()
  date = models.DateTimeField(auto_now_add=True)
  thumb = models.ImageField(default="jay.png", blank=True)
  #add in author later
  
  def __str__(self):
    return self.title

  def snippet(self):
    return self.body[:50] + '...'

#For About Section
class Cover(models.Model):
  name = models.CharField(max_length=50)
  profession = models.CharField(max_length=50)
  description = RichTextField()

class Novel(models.Model):
  title_1 = models.CharField(max_length=50)
  cover_1 = models.ImageField()
  blurb_1 = models.TextField()

class Novella(models.Model):
  title_1 = models.CharField(max_length=50)
  cover_1 = models.ImageField()
  blurb_1 = models.TextField()


class Short(models.Model):
  title_1 = models.CharField(max_length=50)
  cover_1 = models.ImageField()
  blurb_1 = models.TextField()


class Event(models.Model):
  event_1 = models.CharField(max_length=50)
  event_picture_1 = models.ImageField()
  description_1 = models.TextField()
  link_1 = models.URLField()


class Podcast(models.Model):
  title = models.CharField(max_length=50)
  description = models.TextField()

class Feature(models.Model):
  title = models.CharField(max_length=50)
  cover = models.ImageField()
  blurb = RichTextField()



#For categories in the Works section
  #python manage.py migrate
  #python manage.py makemigrations

