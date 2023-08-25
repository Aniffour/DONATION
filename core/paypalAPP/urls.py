from django.urls import path 
from . import views


urlpatterns = [
    path('' , views.Home.as_view() , name='paypal-home')  , 
    path('success/' , views.Success.as_view() , name='paypal-success')  , 
    path('failed/' , views.Failed.as_view() , name='paypal-failed')  , 
]
