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


def send_message_from_bot():

    URL = "https://api.groupme.com/v3/bots/post?token=66fb4770467d0137eb6a227a6d5f8ad6"
    PARAMS = {
            'bot_id': bot_id,
            'text': random.choice(all_tweets) 
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code) 
    time.sleep(1) 



get_trump_tweets() 
print(all_tweets)



