from django.db import models
from django.utils import timezone
# Create your models here.


class Bot(models.Model):
    bot_id = models.CharField(max_length=50)
    name = models.CharField(max_length=50) 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self): 
        return self.name


class Insult(models.Model):
    insult = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.insult


