from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Insult
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import random
from .models import Bot
from datetime import datetime
# Create your views here.

access_token = '66fb4770467d0137eb6a227a6d5f8ad6'
bot_id = '4769d6cbbf0f7a4a3b547746c1'
insults = [] 


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


def send_message_from_bot(botid, selected_insult):
    URL = "https://api.groupme.com/v3/bots/post?token=66fb4770467d0137eb6a227a6d5f8ad6"

    PARAMS = {
            'bot_id': botid,
            'text': selected_insult
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code)
    print('sent %s' % selected_insult)





def view_insults(request):
    template_name = 'insultbot/insults.html'

    insults = Insult.objects.all().order_by('-date_posted')

    context = {
            'insults': insults
            }


    return render(request, template_name, context) 

def bots(request):
    
    template_name = 'insultbot/bots.html' 

    bots = Bot.objects.all().order_by('-date_posted')

    context = {
            'bots': bots
            }

    return render(request, template_name, context) 



def bot_detail(request, pk):
    
    template_name = 'insultbot/bot_detail.html' 

    bot_detail = Bot.objects.filter(pk=pk)

    bot = get_object_or_404(Bot, pk=pk)

    insults = Insult.objects.all().order_by('-date_posted')


    context = {
            'bot': bot, 
            'insults': insults
            }

    return render(request, template_name, context) 



def timed_message(selected_bot_id):
    time_checker = datetime.now() 
    current_time = time_checker.strftime("%H:%M:%S")

    select_insult = random.choice(insults)
    if Insult.objects.filter(insult=select_insult).exists() == True:
        print('Already used')

    if Insult.objects.filter(insult=select_insult).exists() == False:
        if current_time == "02:13:20" or current_time == "02:14:20" or current_time == "02:15:00":
            send_message_from_bot(bot_id, select_insult)
            insultmodel = Insult()
            insultmodel.insult = select_insult
            insultmodel.save()
            time.sleep(1)
        else:
            print("Do nothing %s" % current_time) 

@csrf_exempt
def start_bot(request):

    bot_id = request.POST.get('bot_id')

    get_insults()

    while True:
        timed_message(bot_id)

    return redirect('insult/bots')


