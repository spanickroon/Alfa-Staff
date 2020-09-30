"""This module contain class for work with ProductCard and Purchase object in admin panel."""

from django.contrib import admin

from .models import ProductCard, Purchase


@admin.register(ProductCard)
class AuthorAdmin(admin.ModelAdmin):
    """ProductCard class with list of filters."""

    list_filter = ('name', 'cost',)


@admin.register(Purchase)
class AuthorAdmin(admin.ModelAdmin):
    """Purchase class with list of filters."""

    list_filter = ('user', 'name', 'cost', 'date_buy', 'status',)

    def save_model(self, request, obj, form, change):
        """If status = 2 we returned points on account and update balance."""
        if change:
            if obj.status == 2:
                obj.user.profile.money += obj.cost
                obj.user.profile.save()
                obj.balance += obj.cost
        obj.save()
