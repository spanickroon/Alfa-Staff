"""alfastaff URL Configuration."""

from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('alfastaff_account.urls')),
    path('', include('alfastaff_bonuses.urls')),
    path('', include('alfastaff_shedule.urls')),
]
