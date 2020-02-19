from django.contrib import admin
from .models import Bot, Tweet, Insult, Meme, MemeURL
# Register your models here.
admin.site.register(Tweet)
admin.site.register(Insult)
admin.site.register(Meme)
admin.site.register(Bot)
admin.site.register(MemeURL)