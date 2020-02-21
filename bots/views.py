from __future__ import unicode_literals
from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Max
from django.views.decorators.csrf import csrf_exempt
from  .models import Bot, Tweet, Insult, MemesSent, MemeURL, GMUrl
from .forms import BotForm
import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import random
from datetime import datetime

THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
access_token_file = os.path.join(THIS_FOLDER, 'access-token.txt')
for line in access_token_file:
    fields = line.strip().split()

access_token = fields[0]

all_tweets = []
memes = []
groupme_image_urls = []
insults = []

##########################################################
#METHOD FOR SENDING
##########################################################
def send_message_from_bot(botid, message):
    URL = "https://api.groupme.com/v3/bots/post?token=%s" % access_token

    PARAMS = {
            'bot_id': botid,
            'text': message,
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code) 
    print('sent %s' % message) 

##########################################################
#METHODS FOR GRABBING DATA
##########################################################

categories = ['americana',
        'artoftrolling',
        'cringe',
        'photobombs',
        'pictureisunrelated',
        'politics',
        'puns',
        'ragecomics'] 

category_set = categories[0]  

def get_memes():
    index = 0
    for x in range(len(categories)):
        category_set = categories[index] 
        print('set category %s' % category_set) 
        url = "https://memebase.cheezburger.com/%s" % category_set
        print(url) 
        response_status  = requests.get(url) 
        soup = BeautifulSoup(response_status.text, "html.parser")
        posts = soup.find_all("div", {"class": "resp-media-wrap"})
        print('ALL LINKS FOR %s' % category_set) 
        for post in posts:
            image =  post.find("img")
            meme_link = image.get("data-src")
            print(meme_link)
            if MemeURL.objects.filter(url=meme_link).exists() == True:
            	print('Already used: ')
            if MemeURL.objects.filter(url=meme_link).exists() == False:
	            memes.append(meme_link)
	            memeurl = MemeURL()
	            memeurl.url = meme_link
	            memeurl.save()

        index = index + 1

def check_image_type(link, index):
    # path would be something like 'home/user/Desktop/groupmebot/bots/memes'
    file_path = '<ENTER PATH IF YOU WANT TO DOWNLOAD IMAGES AGAIN>'
    try:
        check = requests.get(link)
        content_type = check.headers['content-type']
        if content_type == 'image/gif':
            urllib.request.urlretrieve(link, '{}/image-00{}.gif'.format(file_path, index))
        elif content_type == 'image/png':
            urllib.request.urlretrieve(link, '{}/image-00{}.png'.format(file_path, index))
        elif content_type == 'image/jpg':
            urllib.request.urlretrieve(link, '{}/image-00{}.jpg'.format(file_path, index))
        elif content_type == 'image/jpeg':
            urllib.request.urlretrieve(link, '{}/image-00{}.jpeg'.format(file_path,index))
        else:
            print('Unknown')
    except UnicodeEncodeError:
        print('error fam')

def download_all_images():
    image_index = 0
    for meme in memes:
        check_image_type(meme, image_index)
        print(image_index)
        image_index = image_index + 1 
        time.sleep(0.5)

def get_groupme_urls(): 
    url = 'https://image.groupme.com/pictures'
    filepath = '<ENTER PATH IF YOU WANT TO DOWNLOAD IMAGES AGAIN>'
    for r, d, file in os.walk(filepath):
        for x in file:
            if '.jpeg' in x:
                data = open('{}/{}'.format(filepath, x), 'rb').read()
                image_request = requests.post(url, data=data, headers={'Content-Type': 'image/jpeg', 'X-Access-Token': '66fb4770467d0137eb6a227a6d5f8ad6' })
                convert = image_request.text
                load_json = json.loads(convert)
                gurl = load_json.get('payload', {}).get("picture_url",{})
                print(gurl)
                groupme_image_urls.append(gurl)
                urlmodel = GMUrl()
                urlmodel.groupme_url = gurl
                urlmodel.save()
            elif '.gif' in x:
                data = open('{}/{}'.format(filepath, x), 'rb').read()
                image_request = requests.post(url, data=data, headers={'Content-Type': 'image/gif', 'X-Access-Token': '66fb4770467d0137eb6a227a6d5f8ad6' })
                convert = image_request.text
                load_json = json.loads(convert)
                gurl = load_json.get('payload', {}).get("picture_url",{})
                print(gurl)
                urlmodel = GMUrl()
                urlmodel.groupme_url = gurl
                urlmodel.save()
            elif '.png' in x:
                data = open('{}/{}'.format(filepath, x), 'rb').read()
                image_request = requests.post(url, data=data, headers={'Content-Type': 'image/png', 'X-Access-Token': '66fb4770467d0137eb6a227a6d5f8ad6' })
                convert = image_request.text
                load_json = json.loads(convert)
                gurl = load_json.get('payload', {}).get("picture_url",{})
                print(gurl)
                groupme_image_urls.append(gurl)
                urlmodel = GMUrl()
                urlmodel.groupme_url = gurl
                urlmodel.save()
            else: 
                print('Fuck if i know') 


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

def get_insults():
    url = "http://www.robietherobot.com/insult-generator.htm" 
    PARAMS = {
            'class1': 'good', 
            'name': 'generate+another+insult'
            }

    for x in range(0, 100): 
        botQuest = requests.post(url, PARAMS)
        soup = BeautifulSoup(botQuest.text, "html.parser") 
        form = soup.find("form")
        insult = form.find("h1")
        finalinsult = insult.text
        spaces = finalinsult.strip()
        insult = "Joe Tang is a: " + spaces
        insults.append(insult)

    print('got em' )

##########################################################
#METHODS FOR TIMED MESSAGES
##########################################################
def timed_insult_message(selected_bot_id):
    time_checker = datetime.now() 
    current_time = time_checker.strftime("%H:%M:%S")

    select_insult = random.choice(insults)
    if Insult.objects.filter(insult=select_insult).exists() == True:
        print('Already used')

    if Insult.objects.filter(insult=select_insult).exists() == False:
        #This is where you edit the times for the insult bot
        if current_time == "08:00:00" or current_time == "20:00:00":
            send_message_from_bot(selected_bot_id, select_insult)
            insultmodel = Insult()
            insultmodel.insult = select_insult
            insultmodel.save()
            time.sleep(1)
        else:
            print("Do nothing %s" % current_time)

def timed_tweet_message(selected_bot_id):
    time_checker = datetime.now() 
    current_time = time_checker.strftime("%H:%M:%S")

    select_tweet = random.choice(all_tweets)
    if Tweet.objects.filter(tweet=select_tweet).exists() == True:
        print('Already used')

    if Tweet.objects.filter(tweet=select_tweet).exists() == False:
        #This is where you edit the times for the tweet bot. Times that are currently set, 8AM and 8PM 
        if current_time == "08:00:00" or current_time == "20:00:00":
            send_message_from_bot(selected_bot_id, select_tweet)
            tweetmodel = Tweet()
            tweetmodel.tweet = select_tweet
            tweetmodel.save()
            time.sleep(1)
        else:
            print("Do nothing %s" % current_time)

def timed_meme_message(selected_bot_id):
    time_checker = datetime.now() 
    current_time = time_checker.strftime("%H:%M:%S")

    max_id = GMUrl.objects.all().aggregate(max_id=Max("id"))['max_id']
    pk = random.randint(1, max_id) 
    url = GMUrl.objects.filter(pk=pk).first() 
    if url:
        select_meme = url
 
        if MemesSent.objects.filter(groupme_url=select_meme).exists() == True:
            print('Already used')

        if MemesSent.objects.filter(groupme_url=select_meme).exists() == False:
            #This is where you edit the times for the meme bot
            if current_time == "16:20:00":
                send_message_from_bot(selected_bot_id, select_meme)
                model = MemesSent()
                model.groupme_url = select_meme
                model.save()
                time.sleep(3)
            else:
                print("Do nothing %s" % current_time)

            #ALTERNATIVELY YOU COULD JUST DO THIS
            #send_message_from_bot(selected_bot_id, select_meme)
            #model = MemesSent()
            #model.groupme_url = select_meme
            #model.save()
            #time.sleep(3) Set the timing however you please

##########################################################
#VIEW DATA THAT IS BEING STORED
##########################################################
def view_insults(request):
    template_name = 'bots/insults.html'
    insults = Insult.objects.all().order_by('-date_posted')
    context = {
            'insults': insults
            }

    return render(request, template_name, context) 

def view_tweets(request):
    template_name = 'bots/tweets.html'
    tweets = Tweet.objects.all().order_by('-date_posted')
    context = {
            'tweets': tweets
            }

    return render(request, template_name, context) 

##########################################################
#VIEW BOTS
##########################################################
def bots(request):
    template_name = 'bots/bots.html' 
    bots = Bot.objects.all().order_by('-date_posted')
    context = {
            'bots': bots
            }

    return render(request, template_name, context) 

def bot_detail(request, pk):
    template_name = 'bots/bot_detail.html' 
    bot_detail = Bot.objects.filter(pk=pk)
    bot = get_object_or_404(Bot, pk=pk)
    #prob will add some bot -> Insult/Tweet/Meme foreign key relationship
    insults = Insult.objects.all().order_by('-date_posted')
    tweets = Tweet.objects.all().order_by('-date_posted')
    memes = MemesSent.objects.all().order_by('-date_posted')

    context = {
            'bot': bot, 
            'insults': insults,
            'memes': memes, 
            'tweets': tweets
            }

    return render(request, template_name, context) 

def add_bot(request):
    template_name = 'bots/add_bot.html'

    if request.method == "POST":
        bot_form = BotForm(request.POST)
        if bot_form.is_valid():
            bot = bot_form.save(commit=False)
            bot.save()
    else:
        bot_form = BotForm() 

    context = {
            'bot_form': bot_form
            }

    return render(request, template_name, context)

##########################################################
#START BOTS
##########################################################
@csrf_exempt
def start_trump_bot(request):
    bot_id = request.POST.get('bot_id')
    get_trump_tweets()
    while True:
        timed_tweet_message(bot_id)
    
    return redirect('/bots/list/')

@csrf_exempt
def start_insult_bot(request):
    bot_id = request.POST.get('bot_id')
    get_insults()
    while True:
        timed_insult_message(bot_id)

    return redirect('/bots/list')

#DO NOT HIT THIS URL, IT WILL GIVE YOU ERRORS,  This is what was used to get all the images
#for this to work, edit the image path for the "GET GROUPME URLS and CHECK IMAGE TYPE" methods
#edit the path to YOUR MACHINE so you can locally download memes
#the memes are already scraped and in the memes folder so you don't really need to do this
def scrape_memes(request): 
    template_name = 'bots/scrape.html' 
    if request.method == "GET":
        get_memes() 
        download_all_images()
        get_groupme_urls() 

    return render(request, template_name) 

@csrf_exempt
def start_meme_bot(request):
    bot_id = request.POST.get('bot_id')

    while True:
        timed_meme_message(bot_id) 


    return redirect('/bots/list')
