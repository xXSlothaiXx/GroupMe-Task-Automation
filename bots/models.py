from django.db import models
from django.utils import timezone
# Create your models here.


class Bot(models.Model):
    bot_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self): 
        return self.name


#Data storage for certain bot messages
class Insult(models.Model):
    insult = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.insult

class Tweet(models.Model):
    tweet = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.tweet


class Meme(models.Model):
    meme = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.meme

class MemeURL(models.Model):
    url = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.url

class GMUrl(models.Model):
    groupme_url = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 


    def __str__(self): 
        return self.groupme_url
