from paypal.standard.models import ST_PP_COMPLETED
from paypal.standard.ipn.signals import valid_ipn_received
from django.core.mail import   send_mail
import logging
from dotenv import load_dotenv
import os

load_dotenv()
logger = logging.getLogger(__name__)

def success_donation(sender, **kwargs):
    ipn_obj = sender
    if ipn_obj.payment_status == ST_PP_COMPLETED:
        if ipn_obj.receiver_email != os.getenv('BUISNESS_EMAIL'):
            # Not a valid payment
            return
        inv = ipn_obj.custom
        amount  =str( ipn_obj.mc_gross) + ' ' + ipn_obj.mc_currency
        send_mail(
            subject='donation !!' , 
            message=f'donation from DONATION WEB SITE . Invoice {inv} and amount : {amount} , receiver email : {ipn_obj.receiver_email}', 
            recipient_list= [ipn_obj.receiver_email , os.getenv('RECEIVER_EMAIL')]
        )        
        log = logging.getLogger('success-payment') 
        log.critical(f'Invoice {inv} and amount : {amount} , receiver email : {ipn_obj.receiver_email} , {os.getenv("RECEIVER_EMAI")}' )
        
    else:
        pass

valid_ipn_received.connect(success_donation)