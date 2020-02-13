import time
import requests
import time
import json
import os
from bs4 import BeautifulSoup
import urllib.request as urllib2
import random
import re
import sys
import json
from google_images_download import google_images_download


url = "https://giphy.com/search/crying-jordan"
response_status  = requests.get(url) 
soup = BeautifulSoup(response_status.text, "html.parser") 
links = soup.findAll("img")
for link in links:
    print(link["src"]) 


