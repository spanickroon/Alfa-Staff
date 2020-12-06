"""This module contain class for work with Task object in admin panel."""

from django.contrib import admin

from .models import Task


@admin.register(Task)
class AuthorAdmin(admin.ModelAdmin):
    """Task class with list of filters."""
    pass