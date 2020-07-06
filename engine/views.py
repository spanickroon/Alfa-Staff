"""This module contain functions for proccesing requests."""

from django.shortcuts import render


def handler_error_404(request, exception):
    return render(
        request, 'error.html', status=404,
        context={'status_code': 404})


def handler_error_500(request):
    return render(
        request, 'error.html', status=500,
        context={'status_code': 500})
