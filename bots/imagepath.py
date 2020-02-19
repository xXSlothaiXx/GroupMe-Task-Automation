import os

def get_groupme_urls(): 
	filepath = '/home/licentia/Desktop/groupmebot/scraping/testing'
	for r, d, file in os.walk(filepath):
		for x in file:
			print(x)

get_groupme_urls()