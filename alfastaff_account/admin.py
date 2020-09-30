"""This module contain class for work with Profile object in admin panel."""

from django.contrib import admin

from .models import Profile


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    """Profile class with list of filters and meta data."""

    list_filter = (
        'first_name', 'second_name', 'middle_name',
        'status', 'money', 'role',)

    class Meta:
        """Meta data."""

        app_label = 'Аккаунт'
        verbose_name = "Профиль"
        base_manager_name = 'Профиль'
        verbose_name_plural = "Профль"
        db_table = 'Профль'
        default_manager_name = 'Профль'
