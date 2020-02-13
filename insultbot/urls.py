from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^insults/', views.view_insults, name='view-tweets'),
    url(r'^bots/', views.bots, name='view-bots'),
    url(r'^bot/(?P<pk>[\w-]+)/$', views.bot_detail, name='bot-detail'),
    url(r'^start/', views.start_bot, name='start-bot'), 

]
