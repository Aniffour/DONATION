from django.shortcuts import render
from django.urls import reverse
from django.views import View
from paypal.standard.forms import PayPalPaymentsForm
from paypal.standard.forms import PayPalPaymentsForm
import datetime
import logging
logger = logging.getLogger(__name__)

class Home (View): 
    def get(self  , request):
        inv = "invoice-donation-time-"+str(datetime.datetime.now()) 
        paypal_dict = {
        "business": "as5828801@gmail.com",
        "item_name": "donation",
        "invoice": inv,
        "notify_url": request.build_absolute_uri(reverse('paypal-ipn')),
        "return": request.build_absolute_uri(reverse('paypal-success')),
        "cancel_return": request.build_absolute_uri(reverse('paypal-failed')),
        "custom": inv, 
    }
        form = PayPalPaymentsForm(initial=paypal_dict)
        
        return render(request , 'paypal/home.html' ,{'form':form} )


class Success (View): 
    def get(self  , request): 
        log = logging.getLogger('page-paypal-success')
        log.warning(f'success payment page open at :{datetime.datetime.now()}')
        return render(request , 'paypal/success.html')

class Failed (View): 
    def get(self  , request):
        log = logging.getLogger('page-paypal-failed') 
        log.error(f'failed payment page open at :{datetime.datetime.now()}')
        return render(request , 'paypal/failed.html')
