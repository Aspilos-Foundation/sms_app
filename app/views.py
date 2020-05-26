from django.shortcuts import render
from django.views.generic import TemplateView, ListView, CreateView
from app.models import SendSMS
from app.forms import SendSMSForm
from django.urls import reverse_lazy
from app.utils import send_twilio_message
from django.conf import settings 
import datetime
# Create your views here.

# Create your models here.

def index(request): 
    return render(request, 'index.html')
def feed(request): 
    return render(request, 'feed.html')
def upload(request): 
    return render(request, 'upload.html')
def messages(request): 
    return render(request, 'messages.html')
def statistics(request): 
    return render(request, 'statistics.html')
    

class SendSmsCreateView(CreateView):
    model = SendSMS
    form_class = SendSMSForm
    template_name = 'messages.html'
    success_url = reverse_lazy('send_sms')

    def form_valid(self, form):
        number = form.cleaned_data['to_number']
        body = form.cleaned_data['body']
            # call twilio
        sent = send_twilio_message(number, body)
            # save form
        send_sms = form.save(commit=False)
        send_sms.from_number = settings.TWILIO_PHONE_NUMBER
        send_sms.sms_sid = sent.sid
        send_sms.account_sid = sent.account_sid
        send_sms.status = sent.status
        send_sms.sent_at = datetime.datetime.now()
        if sent.price:
            send_sms.price_unit = sent.price_unit
            send_sms.save()

        return super(SendSmsCreateView, self).form_valid(form)