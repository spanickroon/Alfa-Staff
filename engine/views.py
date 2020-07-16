"""This module contain functions for proccesing requests."""

from django.shortcuts import render
import os


def handler_error_404(request, exception):
    return render(
        request, 'error.html', status=404,
        context={
            'status_code': 404,
            'message': 'Страница не найдена',
            'info_error_first': 'Неверный путь в адресной строке',
            'info_error_second': 'Наверное вам стоит вернуться обратно'})


def handler_error_500(request):
    return render(
        request, 'error.html', status=500,
        context={
            'status_code': 500,
            'message': 'Что-то пошло не так',
            'info_error_first': 'Сообщите об этой ошибке на',
            'info_error_second': os.environ.get('EMAIL_HOST_USER')})
