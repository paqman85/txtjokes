
from django import forms
from .models import PhoneModel

class ReceiverForm(forms.ModelForm):
    class Meta:
        model = PhoneModel
        fields = ['phone_number']