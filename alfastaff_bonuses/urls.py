"""This module contain urls for application."""

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
    path('purchases', purchases, name='purchases'),
    path('purchases/<int:page>/<str:sort>', purchases_page, name='purchases_page'),
    path('bonuses', bonuses, name='bonuses'),
    path('bonuses/<int:page>/<str:sort>', bonuses_page, name='bonuses_page'),
    path('buy/<int:id>', buy, name='buy'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
