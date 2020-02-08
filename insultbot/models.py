from django.db import models
from django.utils import timezone
# Create your models here.


class Insult(models.Model):
    insult = models.TextField() 
    date_posted = models.DateTimeField(default=timezone.now) 

    def __str__(self):
        return self.insult
