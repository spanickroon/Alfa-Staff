
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
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', activate, name='activate')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
