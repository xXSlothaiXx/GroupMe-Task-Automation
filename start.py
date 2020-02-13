import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import urllib2
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

def get_soup_google(url, header):
    return BeautifulSoup(urllib2.urlopen(urllib2.Request(url,headers=header)),'html.parser')

def get_google_images():

    url = "https://www.google.co.in/search?q=%s&source=lnms&tbm=isch" % query 

    header={'User-Agent':"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}
    soup = get_soup(url, header)
    
    ActualImages=[]# contains the link for Large original images, type of  image
	for a in soup.find_all("div",{"class":"rg_meta"}):
	    link , Type =json.loads(a.text)["ou"]  ,json.loads(a.text)["ity"]
	    ActualImages.append((link,Type))
	for i , (img , Type) in enumerate( ActualImages[0:max_images]):
	    try:
	        req = urllib2.Request(img, headers={'User-Agent' : header})
	        raw_img = urllib2.urlopen(req).read()
	        if len(Type)==0:
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+".jpg"), 'wb')
	        else :
	            f = open(os.path.join(save_directory , "img" + "_"+ str(i)+"."+Type), 'wb')
	        f.write(raw_img)
	        f.close()
	    except Exception as e:
	        print "could not load : "+img
	        print e


def send_message_from_bot():

    URL = "https://api.groupme.com/v3/bots/post?token=66fb4770467d0137eb6a227a6d5f8ad6"
    PARAMS = {
            'bot_id': bot_id,
            'text': random.choice(all_tweets) 
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code) 
    time.sleep(1) 


def get_group_message(): 
    url = "https://api.groupme.com/v3/groups/52672212/messages?token=66fb4770467d0137eb6a227a6d5f8ad6" 
    start = requests.get(url) 
    print(start.text) 

get_group_message()

