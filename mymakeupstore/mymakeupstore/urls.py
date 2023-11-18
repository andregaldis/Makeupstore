"""
URL configuration for mymakeupstore project.


"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
# En tu archivo urls.py
from django.urls import path
from . import views  # Asegúrate de importar tus vistas

urlpatterns = [
    # otras rutas...
    path('', views.tu_vista_de_productos, name='productos'),
]
