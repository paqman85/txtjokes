TxtJokes

This project is built with Django and Bootstrap 4. This project uses pipenv and docker as virtual environments. TxtJokes was created for the twillio hackathon and uses twillio to send sms messages, and twilio sendgrid for the authentication emails. This project hows how to use Twillio technology for a basic django application. Please feel free to expand upon the project. :)

The demo of the project will be active for a short time on txtjokes.herokuapp.com.


Local Launch

Launch to Heroku



To launch txtjokes locally:
1) Downlod the git repo.

2) Update the environment variables in the docker-compose file with your account information, API, Secret keys, etc.

3) from your terminal, navigate to the txtjokes folder (ex. cd txtjokes)

4) Launch docker-compose to run the site locally. (Ex. docker-compose up -d --build)

5) If you added all of your environment variables correctly, you should have the app runnin on localhost:8000! Congratulations, you're ready to make some dev nerds laugh!


To launch txtjokes to Heroku:
In order to launch on heroku you'll require a heroku acocunt.

Launch to production from your local environment
1) Follow the steps above to get the program working on your local computer.

2) Start a git for the project and save it.
    git init
    git status
    git add .
    git commit -m 'txtjokes initial'

3) Add the environment variables listed in docker-compose to the heroku environment variables section of your heroku app

4) From your command line with Heroku CLI installed. (link to heroku cli)
    Here are the sequence of comands to launch the project on the free tier of heroku.

    heroku login
    
    heroku create  (Take note of the app name -- somthing like 'damp-shield-9932'. Add 'YOUR-HEROKU-APP-NAME.herokuapp.com' to your settings allowed host in the django project.)
    
    heroku stack:set container -a damp-shield-9932  
    (make sure to change the app name to whatever you generated in the previous command - do this everytime you see damp-shield-9932)
    
    heroku addons:create heroku-postgresql:hobby-dev -a damp-shield-9932
    
    heroku git:remote -a damp-shield-9932
    git status
    git add .
    git commit -m 'txtjokes pre-deploy'
    git push heroku master

    heroku run python manage.py migrate

    heroku run python manage.py createsuperuser

    heroku open -a damp-shield-9932

5) Send some jokes!


Some Additional Notes:

Ideas for improvements;
a) Txt counter to show how many jokes were sent.
b) notification bubble to show the joke sent
c) Expanding joke library
d) susbcription service for daily jokes

Spin offs:
This project has everything you need for several types of spin-offs. Only some minor adaptation is needed to spin this into other interesting projects!

a) daily motivation messenger (Don't give up!)
b) reminder service (Don't forget the milk - texted as you leave work)
c) COVID-19 daily info msgs (Daily stats send in brief to your phone)
d) Daily Gifs -- Combine this service with Giphy API
e) Anonymous sms service
d) Daily riddles (24 hours to solve before the anser is sent)
f) Chess by sms - learn to play blind chess with notations
g) Your idea here!