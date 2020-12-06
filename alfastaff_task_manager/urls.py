"""This module contain urls for application."""
from django.urls import path
from django.conf.urls import url

from .views import *

name_apps = 'alfastaff_task_manager'


urlpatterns = [
    path('taskmanager', taskmanager, name='taskmanager'),
]
