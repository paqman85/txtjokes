<h1>TxtJokes</h1>

This project is built with Django and Bootstrap 4. This project uses pipenv and docker as virtual environments. TxtJokes was created for the twillio hackathon and uses twillio to send sms messages, and twilio sendgrid for the authentication emails. This project hows how to use Twillio technology for a basic django application. Please feel free to expand upon the project. :)

The demo of the project will be active for a short time on <a href="txtjokes.herokuapp.com">txtjokes.herokuapp.com</a>.


<a href="#local">Local Launch</a>

<a href="#heroku">Launch to Heroku</a>

<a href="#other">Additional notes</a>



<h3 id="local">To launch txtjokes locally:</h3>
<ol>
    <li>Downlod the git repo.</li>
    <li>Update the environment variables in the docker-compose file with your account information, API, Secret keys, etc.</li>
    <li>From your terminal, navigate to the txtjokes folder (ex. cd txtjokes)</li>
    <li>Launch docker-compose to run the site locally. (Ex. docker-compose up -d --build)</li>
    <li>If you added all of your environment variables correctly, you should have the app runnin on localhost:8000! Congratulations, you're ready to make some dev nerds laugh!</li>
</ol>

<h3 id="heroku">To launch txtjokes to Heroku:</h3>
In order to launch on heroku you'll require a <a href="https://signup.heroku.com/">heroku acocunt</a>.

Launch to production from your local environment:
<ul>
    <li>Follow the steps above to get the program working on your local computer.</li>
    <li>Start a git for the project and save it.</li>
</ul>
```
git init
git status
git add .
git commit -m 'txtjokes initial'
```
<ul>
    <li>Add the environment variables listed in docker-compose to the heroku environment variables section of your heroku app</li>
    <li>From your command line with <a href="https://devcenter.heroku.com/articles/heroku-cli">Heroku CLI installed.</a></li>
        Here are the sequence of comands to launch the project on the free tier of heroku:
        (Take note of the app name -- something like 'damp-shield-9932'. Add 'YOUR-HEROKU-APP-NAME.herokuapp.com' to your settings allowed host in the django project. Make sure to change the app name to whatever you generated in the previous command - do this everytime you see damp-shield-9932)
```
heroku login
heroku create 
heroku stack:set container -a damp-shield-9932
heroku addons:create heroku-postgresql:hobby-dev -a damp-shield-9932
heroku git:remote -a damp-shield-9932
git status
git add .
git commit -m 'txtjokes pre-deploy'
git push heroku master
heroku run python manage.py migrate
heroku run python manage.py createsuperuser
heroku open -a damp-shield-9932
```
    <li>Send some jokes!</li>
</ul>

<h3 id="other">Some Additional Notes:</h3>

<h4>Ideas for improvements:</h4>
<ol>
    <li>Txt counter to show how many jokes were sent.</li>
    <li>Notification bubble to show the joke sent</li>
    <li>Expanding joke library</li>
    <li>Susbcription service for daily jokes</li>
</ol>

<h4>Spin offs:</h4>
This project has everything you need for several types of spin-offs. Only some minor adaptation is needed to spin this into other interesting projects!
<ol>
    <li>Daily motivation messenger (Don't give up!)</li>
    <li>Reminder service (Don't forget the milk - texted as you leave work)</li>
    <li>COVID-19 daily info msgs (Daily stats send in brief to your phone)</li>
    <li>Daily Gifs -- Combine this service with Giphy API</li>
    <li>Anonymous sms service</li>
    <li>Daily riddles (24 hours to solve before the anser is sent)</li>
    <li>Chess by sms - learn to play blind chess with notations</li>
    <li>Your idea here!</li>

This project was created as a one day build by Glenn Paquette, currently operating <a href="https://atomicgrowth.co">Atomic Growth</a> as a submission for the <a href="https://dev.to/t/twiliohackathon">Twilio Hackathon</a> on <a href="https://Dev.to">Dev.to</a>. Background music while coding was supplied by <a href="https://www.youtube.com/channel/UCT5RMcRGa32Th0AZ0Dxxviw">JimTV</a> - Thanks JimTV!