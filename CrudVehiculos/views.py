from django.shortcuts import render, redirect
from .models import Vehiculos
from .forms import VehiculosForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
def registarVehiculos(request):
    vehiculos = Vehiculos.objects.all()
    if request.method == 'POST':
        form = VehiculosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo Registrado Correctamente!')
            return redirect('registarVehiculos')
        else:
            messages.error(request, 'Error al registrar el vehiculo. Por favor, verificar los datos.')
            return render(request,'gestionVehiculos.html', {"form":form, "vehiculos":vehiculos})
    else:
        form = VehiculosForm()
        return render(request,'gestionVehiculos.html', {"form":form, "vehiculos":vehiculos})

def edicionVehiculos(request, vehiculoID):
    vehiculo = Vehiculos.objects.get(vehiculoID=vehiculoID)
    if request.method == 'POST':
        form = VehiculosForm(request.POST, instance=vehiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vehiculo Editado Correctamente!')
            return redirect('registarVehiculos')
        else:
            messages.error(request, 'Error al editar el vehiculo. Por favor, verifica los datos.')
            return render(request, 'edicionVehiculos.html', {'form':form,"vehiculoID":vehiculoID})
    else:
        form = VehiculosForm(instance=vehiculo)
        return render(request, 'edicionVehiculos.html', {'form':form,"vehiculoID":vehiculoID})

def eliminarVehiculos(request, vehiculoID):
    vehiculo = Vehiculos.objects.get(vehiculoID=vehiculoID)
    vehiculo.delete()
    messages.success(request, 'Vehiculo Eliminado Correctamente!')
    return redirect('registarVehiculos')

#Excel

from openpyxl import Workbook
from django.http import HttpResponse

def descargar_vehiculos(request):
    vehiculos = Vehiculos.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.append(['Patente', 'Marca', 'Modelo', 'FechaAdquisicion', 'Estado', 'Comentario'])

    for vehiculo in vehiculos:
        ws.append([vehiculo.patente, vehiculo.marca, vehiculo.modelo, vehiculo.fechaAdquisicion, vehiculo.estado, vehiculo.comentario])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="vehiculos.xlsx"'
    wb.save(response)

    return response