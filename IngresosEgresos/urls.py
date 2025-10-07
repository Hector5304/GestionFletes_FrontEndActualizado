from django.urls import path
from . import views

urlpatterns = [
   path('registrarIngresos/', views.registrarIngresos,name='registrarIngresos'),
   path('editarIngresos/<ingresoID>', views.editarIngresos, name='editarIngresos'),
   path('eliminarIngresos/<ingresoID>', views.eliminarIngresos, name='eliminarIngresos'),
   path('registrarEgresos/', views.registrarEgresos, name='registrarEgresos'),
   path('editarEgresos/<egresoID>', views.editarEgresos, name='editarEgresos'),
   path('eliminarEgresos/<egresoID>', views.eliminarEgresos, name='eliminarEgresos'),
]