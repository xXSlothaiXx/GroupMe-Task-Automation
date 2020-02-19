from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    #listing bots
    url(r'^list/', views.bots, name='view-bots'),
    url(r'^bot/(?P<pk>[\w-]+)/$', views.bot_detail, name='bot-detail'),
    #listing data
    url(r'^tweets/', views.view_tweets, name='view-tweets'), 
    url(r'^insults/', views.view_insults, name='view-tweets'),
    #scraping data 
    url(r'^scrape/', views.scrape_memes, name='scrape-memes'),
    #start bots
    url(r'^starttrump/', views.start_trump_bot, name='start-trump-bot'),
    url(r'^startinsult/', views.start_insult_bot, name='start-insult-bot'),
    url(r'^startmeme/', views.start_meme_bot, name='start-meme-bot'), 
]
