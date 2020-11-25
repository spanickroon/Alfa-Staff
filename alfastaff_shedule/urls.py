"""This module contain urls for application."""

from django.urls import path
from django.conf.urls import url

from .views import *


name_apps = 'alfastaff_shedule'


urlpatterns = [
    path('shedule', shedule, name='shedule'),
    path('review', review, name='review')
]
