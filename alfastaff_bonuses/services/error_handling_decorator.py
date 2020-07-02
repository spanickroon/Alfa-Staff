"""This module contain functions for error handling."""

from django.http import Http404


def error_handling(func):
    """Error handling."""
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as ex:
            return Http404
    return inner
