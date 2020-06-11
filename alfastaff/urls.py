
from django.urls import path
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.http import HttpResponse


def test(request):
    return HttpResponse('test')


urlpatterns = [
    path('', test),
]
