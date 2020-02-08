from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Insult
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request
import random

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


def send_message_from_bot(selected_insult):
    URL = "https://api.groupme.com/v3/bots/post?token=66fb4770467d0137eb6a227a6d5f8ad6"

    PARAMS = {
            'bot_id': bot_id,
            'text': selected_insult
            }
    send_message = requests.post(URL, PARAMS)
    print(send_message.status_code)
    print('sent %s' % selected_insult)


def cycle_insults():
    index = 0
    for x in range(len(insults)):
        select_insult = insults[index]
        if Insult.objects.filter(insult=select_insult).exists() == True:
            print('Already used')
            index = index + 1

        if Insult.objects.filter(insult=select_insult).exists() == False:
            send_message_from_bot(select_insult)
            insultmodel = Insult()
            insultmodel.insult = select_insult
            insultmodel.save()
            index = index + 1
            time.sleep(2)



def view_insults(request):
    template_name = 'insultbot/insults.html'

    insults = Insult.objects.all().order_by('-date_posted')

    context = {
            'insults': insults
            }


    return render(request, template_name, context) 

@csrf_exempt
def start_bot(request):

    get_insults()
    cycle_insults() 
    
    return redirect('/insult/insults/')
