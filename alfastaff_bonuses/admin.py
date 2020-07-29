"""This module contain class for work with BonusCard and Purchase object in admin panel."""

from django.contrib import admin

from .models import BonusCard, Purchase


@admin.register(BonusCard)
class AuthorAdmin(admin.ModelAdmin):
    """BonusCard class with list of filters."""

    list_filter = ('name', 'cost',)

    def save_model(self, request, obj, form, change):
        """Conver image to image binary."""
        try:
            obj.image_binary = form.cleaned_data.get('image').read()
        except:
            obj.image_binary = open("static/images/site/product.jpg", "rb").read()
        obj.save()


@admin.register(Purchase)
class AuthorAdmin(admin.ModelAdmin):
    """Purchase class with list of filters."""

    list_filter = ('user', 'name', 'cost', 'date_buy', 'status',)

    def save_model(self, request, obj, form, change):
        """If status = 2 we returned points on account and update balance."""
        if change:
            if obj.status == 2:
                obj.user.profile.points += obj.cost
                obj.user.profile.save()
                obj.balance += obj.cost
        obj.save()
