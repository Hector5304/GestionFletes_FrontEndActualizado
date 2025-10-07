from django.urls import path
from . import views

urlpatterns = [
   path('registrarRecorridos/', views.registrarRecorridos,name='registrarRecorridos'),
   path('editarRecorridos/<recorridoID>', views.editarRecorridos, name='editarRecorridos'),
   path('eliminarRecorridos/<recorridoID>', views.eliminarRecorridos, name='eliminarRecorridos'),
   path('descargarRecorridos/', views.descargarRecorridos, name='descargarRecorridos'),
   path('detalleRecorrido/<recorridoID>/', views.detalleRecorrido, name='detalleRecorrido'),
   path('detalleGastoBencina/<recorridoID>/', views.detalleGastoBencina, name='detalleGastoBencina'),
]
