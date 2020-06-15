
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *

name_apps = 'alfastaff'

urlpatterns = [
    path('', login, name='login'),
    path('login', login, name='login'),
    path('signup', signup, name='signup'),
    path('logout', logout, name='logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
