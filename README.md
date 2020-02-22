
# GroupMe-Task-Automation
This is a full stack GroupMe API application

## Retrieve GroupMe Access Token
### Sign Up for GroupMe
https://web.groupme.com/signup
### Go to GroupMe Developers Site and get your access token
https://dev.groupme.com
### Create a GroupMe Bot
https://dev.groupme.com/bots

Save your Bot ID for later reference. You will use those bot id's to add it your Django Database
Once you have your access token and a valid bot id you can set up the Django Application

## SETUP TASK AUTOMATION
This application requires Python 3++ and the Django Web Framework

### Django Framework setup
https://docs.djangoproject.com/en/3.0/topics/install/

### Install Crispy Forms for Django
Install django crispy forms module
```
pip3 install django-crispy-forms
```

### Make Migrations On Django Application
```
python3 manage.py migrate
```
Then create a superuser and enter a username and password to access your database
```
python3 manage.py createsuperuser
```
Lastly make migrations on the BOTS app and the django application

```
python3 manage.py makemigrations bots
python3 manage.py makemigrations
python manage.py migrate  (Again)
```

### Configure your ACCESS TOKEN in the Django Application
Type this command in the Django application and enter your GroupMe Access token 

```
python3 access-token.py
```
Once you've set your access token, you can run the Django Server
```
python3 manage.py runserver
```

## Navigating the WEB APP

### Getting your memes and URL's 
Go to http://127.0.0.1:8000/bots/scrape and scrape the memes. If it's working you should see groupme urls pop up in the terminal. Wait till it is done so that all the urls will be added to the database. Once it's done you can go to http://127.0.0.1:8000/admin -> login and see if the urls loaded under the GMUrls model 

### Adding bots
Go to http://127.0.0.1:8000/bots/create to enter your bot name and bot id

### Viewing Bot's
Go to http://127.0.0.1:8000/bots/list to see all your bots. Click on the bot and it should bring you to another page with a few options

### Using the message sending options
There are  options that you can use on the web app to send certain types of messages with certain time limtits

### You can only select ONE option
Once you select your option, Press Start Bot and let the applciation run in the background, The app will show a loading sign in the browser. Leave this page open and open another tab to see what your bot has sent 

#### Trump Tweet Bot Option
This option will send a tweet from Donald Trump Everyday at 8:00 AM/PM

#### Insult Bot Option
This option will generate random insults and your bot will send them everyday at 8AM/PM

#### The Meme Option
This option will send memes from the /memes directory and the django Application. This will send random memes everyday at 4:20 pm

### Loop message options (For Testing) 
If you use one of the loop testing methods, it will send messages every 60 seconds to make sure your access token is working

#### Editing the time stamps
If you want to edit the timing of your messages for the bots. Go to the views.py fle in the bots application and go to lines 193-194, 212-213, 236-237 and change the times to whatever you want
