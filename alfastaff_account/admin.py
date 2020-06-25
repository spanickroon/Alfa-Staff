from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = (
        'first_name', 'second_name', 'middle_name',
        'status', 'points', 'role',)

    class Meta:
        app_label = 'Аккаунт'
        verbose_name = "Профиль"
        base_manager_name = 'Профиль'
        verbose_name_plural = "Профль"
        db_table = 'Профль'
        default_manager_name = 'Профль'
