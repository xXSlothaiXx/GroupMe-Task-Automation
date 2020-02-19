import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen
import random
import re
import sys
import json
from google_images_download import google_images_download

def get_images():

    url = "https://giphy.com/search/crying-jordan"
    html = urlopen(url) 
    response_status  = requests.get(url) 
    soup = BeautifulSoup(html, "html.parser") 
    images = soup.find_all('img') 
    for image in images:
        print(image['src']+'\n')

get_images()


