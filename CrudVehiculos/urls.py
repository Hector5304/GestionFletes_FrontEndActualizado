from django.urls import path
from . import views

urlpatterns = [
    path('registarVehiculos/', views.registarVehiculos, name='registarVehiculos'),
    path('edicionVehiculos/<vehiculoID>/', views.edicionVehiculos, name="edicionVehiculos"),
    path('eliminarVehiculos/<vehiculoID>/', views.eliminarVehiculos, name="eliminarVehiculos"),
    path('descargar_vehiculos/', views.descargar_vehiculos, name='descargar_vehiculos'),
]