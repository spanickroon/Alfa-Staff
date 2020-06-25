from django.contrib import admin
from .models import BonusCard, Purchase


@admin.register(BonusCard)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('name', 'cost',)


@admin.register(Purchase)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ('user', 'name', 'cost', 'date_buy', 'status',)
