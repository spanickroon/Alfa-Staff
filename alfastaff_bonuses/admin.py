"""This module contain class for work with BonusCard and Purchase object in admin panel."""

from django.contrib import admin
from .models import BonusCard, Purchase


@admin.register(BonusCard)
class AuthorAdmin(admin.ModelAdmin):
    """BonusCard class with list of filters."""

    list_filter = ('name', 'cost',)


@admin.register(Purchase)
class AuthorAdmin(admin.ModelAdmin):
    """Purchase class with list of filters."""

    list_filter = ('user', 'name', 'cost', 'date_buy', 'status',)
