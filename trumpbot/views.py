# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from  .models import Tweet
# Create your views here.
import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import random



access_token = '66fb4770467d0137eb6a227a6d5f8ad6'
bot_id = '8e197b688d226003062450ee82' 
all_tweets = []

#set times for a donald trump tweet to be sent
#send the tweet
#if the tweet has been sent before, do not send it
all_tweets = [] 

def get_trump_tweets():
    url = "https://twitter.com/realDonaldTrump"
    response_status  = requests.get(url) 
    soup = BeautifulSoup(response_status.text, "html.parser") 
    tweets = soup.find_all("li", {"data-item-type": "tweet"}) 
    for tweet in tweets:
        tweet_text_box = tweet.find("p", {"class": "TweetTextSize TweetTextSize--normal js-tweet-text tweet-text"})
        tweet_id = tweet_text_box.text 
        all_tweets.append(tweet_id) 
    print('got em')


        
def send_message_from_bot(selected_tweet):
    URL = "https://api.groupme.com/v3/bots/post?token=66fb4770467d0137eb6a227a6d5f8ad6"

    PARAMS = {
            'bot_id': bot_id,
            'text': selected_tweet
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code) 
    print('sent %s' % selected_tweet) 


def cycle_tweets():
    index = 0 
    for x in range(len(all_tweets)):
        select_tweet = all_tweets[index]
        if Tweet.objects.filter(tweet=select_tweet).exists() == True:
            print('Already used')
            index = index + 1

        if Tweet.objects.filter(tweet=select_tweet).exists() == False: 
            send_message_from_bot(select_tweet) 
            tweetmodel = Tweet()
            tweetmodel.tweet = select_tweet 
            tweetmodel.save()
            index = index + 1
            time.sleep(1400) 

def view_tweets(request):
    template_name = 'trumpbot/tweets.html'

    tweets = Tweet.objects.all().order_by('-date_posted')

    context = {
            'tweets': tweets
            }


    return render(request, template_name, context) 

@csrf_exempt
def start_bot(request):

    get_trump_tweets()
    cycle_tweets() 
    


    return redirect('/trump/tweets/')
