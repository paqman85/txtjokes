import pyjokes
import sys
import phonenumbers
from twilio.rest import Client

from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib import messages

from .forms import ReceiverForm



class HomePageView(TemplateView):
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'

def sendjoke(request):

    # Bring in variables for Twilio
    
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        joke = pyjokes.get_joke()
        account_sid = settings.TWILIO_ACC_SID
        auth_token = settings.TWILIO_AUTH_TOKEN

        client = Client(account_sid, auth_token)
        # create a form instance and populate it with data from the request:
        form = ReceiverForm(request.POST)
        tel=(form.data['phone_number'])
        # tel= phonenumbers.format_number(form.data['phone_number'], phonenumbers.PhoneNumberFormat.E164)
        print(form)
        # check whether it's valid:
        if form.is_valid():
            message = client.messages \
                .create(
                    body=joke,
                    messaging_service_sid=settings.TWILIO_MSG_SERVICE_SID,
                    to=tel
            )
            print(message.sid)
        
            return render(request,'thanks.html')
        else:
            messages.error(request, "Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.")
           
        return render(request, 'joke.html', {'form': form})
    # if a GET (or any other method) we'll create a blank form
    else:
        form = ReceiverForm()

    return render(request, 'joke.html', {'form': form})