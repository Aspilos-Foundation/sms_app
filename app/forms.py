from django import forms
from .models import SendSMS
from django.conf import settings

class SendSMSForm(forms.ModelForm):
    class Meta:
        model = SendSMS
        fields = ('to_number', 'body')

