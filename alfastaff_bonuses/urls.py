from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *

name_apps = 'alfastaff-bonuses'

urlpatterns = [
    path('profile', profile, name='profile'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)