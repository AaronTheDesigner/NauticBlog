from django.contrib import admin
from .models import Article, Cover, Novel, Event, Podcast, Novella, Short

# Register your models here.
admin.site.register(Article)
admin.site.register(Cover)
admin.site.register(Novel)
admin.site.register(Event)
admin.site.register(Podcast)
admin.site.register(Novella)
admin.site.register(Short)

