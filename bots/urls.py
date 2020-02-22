from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    #create bot
    url(r'^create/', views.add_bot, name='add-bot'),
    #listing bots
    url(r'^list/', views.bots, name='view-bots'),
    url(r'^bot/(?P<pk>[\w-]+)/$', views.bot_detail, name='bot-detail'),
    #scraping data 
    url(r'^scrape/', views.scrape_memes, name='scrape-memes'),
    #start bots
    url(r'^starttrump/', views.start_trump_bot, name='start-trump-bot'),
    url(r'^startinsult/', views.start_insult_bot, name='start-insult-bot'),
    url(r'^startmeme/', views.start_meme_bot, name='start-meme-bot'), 

     #start loop message bots
    url(r'^trumpspam/', views.start_60_second_trump_bot, name='start-60second-trump-bot'),
    url(r'^insultspam/', views.start_60_second_insult_bot, name='start-60second-insult-bot'),
    url(r'^memespam/', views.start_60_second_meme_bot, name='start-60second-meme-bot'),

]
