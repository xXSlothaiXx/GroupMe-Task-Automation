import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import urllib.request
import random
import re
import sys
import json
import pandas as pd

#we are building a meme bot
#we will get the links from the memes
#and then we will we add it to the database 
file_path = 'images/'

image_array = []

categories = ['americana',
        'artoftrolling',
        'cringe',
        'photobombs',
        'pictureisunrelated',
        'politics',
        'puns',
        'ragecomics'] 

category_set = categories[0]  

def urls_to_image(i, url, path):

    file = 'image-{}.png'.format(i)
    full_path = '{}{}'.format(file_path, file)
    urllib.request.urlretrieve(url, full_path)


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
            image_array.append(meme_link)
            
        index = index + 1


def check_image_type(link, index):
    file_path = 'testing'
    try:
        check = requests.get(link)
        content_type = check.headers['content-type']
        if content_type == 'image/gif':
            urllib.request.urlretrieve(link, '{}/image-{}.gif'.format(file_path, index))
        elif content_type == 'image/png':
            urllib.request.urlretrieve(link, '{}/image-{}.png'.format(file_path, index))
        elif content_type == 'image/jpg':
            urllib.request.urlretrieve(link, '{}/image-{}.jpg'.format(file_path, index))
        elif content_type == 'image/jpeg':
            urllib.request.urlretrieve(link, '{}/image-{}.jpeg'.format(file_path,index))
        else:
            print('Unknown')
    except UnicodeEncodeError:
        print('error fam')


def download_all_images():
    image_index = 0
    for image in image_array:
        check_image_type(image, image_index)
        print(image_index)
        image_index = image_index + 1 
        time.sleep(0.5)
        
get_memes()
download_all_images()



