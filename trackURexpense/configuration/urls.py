from django.urls import include, path

from configuration.admin import admin_site


urlpatterns = [
    path('home/', admin_site.urls),
    path('api/', include('users.router')),
]
