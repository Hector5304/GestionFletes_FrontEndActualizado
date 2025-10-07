"""
URL configuration for Fletes project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Rutas de las aplicaciones de gestión
    path('vehiculos/', include('CrudVehiculos.urls')),
    path('conductores/', include('CrudConductores.urls')),
    path('mantenciones/', include('CrudMantenciones.urls')),
    path('recorridos/',include('CrudRecorridos.urls')),
    path('IngEgr/',include('IngresosEgresos.urls')),

    # El dashboard es ahora la página principal después del login
    path('dashboard/',include('Balance.urls')),
    
    # La antigua página de inicio, por si la necesitas
    path('home/', include('Home.urls')), 
    
    # Las rutas de autenticación (login, logout, registro) están en la raíz
    path('', include('Cuentas.urls')), 
]