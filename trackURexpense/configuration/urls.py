from django.urls import path

from configuration.admin import admin_site


urlpatterns = [
    path('home/', admin_site.urls),
]
