from .models import Bot
from django import forms

class BotForm(forms.ModelForm):

    class Meta:
        model = Bot
        fields = ['name', 'bot_id']
        exclude = ['date_posted']
