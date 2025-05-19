from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import create_admin_user  # Import the new view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create-admin/', create_admin_user),  # Temporary superuser creation URL
    path('', include('core.urls')),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
