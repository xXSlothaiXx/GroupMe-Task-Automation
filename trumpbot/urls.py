from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^tweets/', views.view_tweets, name='view-tweets'), 

    url(r'^start/', views.start_bot, name='start-bot'),  
]