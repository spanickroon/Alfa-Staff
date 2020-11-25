"""alfastaff URL Configuration."""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
from .views import handler_error_404, handler_error_500


admin.site.site_header = 'Админ панель Альфа-Персонал'

urlpatterns = [
    path('admin/', admin.site.urls, name="admin"),
    path('', include('alfastaff_account.urls')),
    path('', include('alfastaff_products.urls')),
    path('', include('alfastaff_shedule.urls')),
    path('', include('alfastaff_task_manager.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


handler404 = handler_error_404
handler500 = handler_error_500
