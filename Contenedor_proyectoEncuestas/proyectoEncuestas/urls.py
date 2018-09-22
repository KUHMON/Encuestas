# proyectoEncuestas/urls.py

from django.urls import include, path
from django.conf.urls import url
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('appEncuestas/', include('appEncuestas.urls')),
]

