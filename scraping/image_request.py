import requests
import time
import json

url = 'https://image.groupme.com/pictures'
data = open('image-1.jpeg', 'rb').read()
image_request = requests.post(url, data=data, headers={'Content-Type': 'image/jpeg', 'X-Access-Token': '66fb4770467d0137eb6a227a6d5f8ad6' })
convert = image_request.text
load_json = json.loads(convert)
gurl = load_json.get('payload', {}).get("url",{})
print(gurl)