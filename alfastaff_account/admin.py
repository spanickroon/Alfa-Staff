"""This module contain class for work with Profile object in admin panel."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    """Profile class with list of filters and meta data."""

    list_filter = (
        'first_name', 'second_name', 'middle_name',
        'status', 'points', 'role',)

    class Meta:
        """Meta data."""

        app_label = 'Аккаунт'
        verbose_name = "Профиль"
        base_manager_name = 'Профиль'
        verbose_name_plural = "Профль"
        db_table = 'Профль'
        default_manager_name = 'Профль'

    def save_model(self, request, obj, form, change):
        """Conver avatar to avatar binary."""
        try:
            obj.avatar_binary = form.cleaned_data.get('avatar').read()
        except Exception:
            obj.avatar_binary = open("static/images/site/user_anon.png", "rb").read()
        obj.save()
