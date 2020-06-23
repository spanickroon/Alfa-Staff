from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from .views import *

name_apps = 'alfastaff-bonuses'

urlpatterns = [
    path('profile', profile, name='profile'),
    path('logout', logout_user, name='logout'),
    path('edit', edit, name='edit'),
    path('edit_profile', edit_profile, name='edit_profile'),
    path('edit_password', edit_password, name='edit_password'),
    path('list_purchese', list_purchese, name='list_purchese'),
    path('bonuses', bonuses, name='bonuses'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)