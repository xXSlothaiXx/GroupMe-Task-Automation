# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.db import models

# Create your models here.

class Tweet(models.Model):
    tweet = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.tweet

