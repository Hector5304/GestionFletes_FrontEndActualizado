from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Mantenciones
from .forms import MantencionForm
from django.contrib.auth.decorators import login_required

@login_required
def registrarMantenciones(request):
    mantenciones = Mantenciones.objects.all()
    if request.method == 'POST':
        form = MantencionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Registrada Correctamente!')
            return redirect('registrarMantenciones')
        else:
            messages.error(request, 'Error al registrar la mantencion. Por favor, verificar los datos.')
            return render(request,'gestionMantenciones.html', {"form":form, "mantenciones":mantenciones})
    else:
        form = MantencionForm()
        return render(request,'gestionMantenciones.html', {"form":form, "mantenciones":mantenciones})

def editarMantenciones(request, mantencionID):
    mantencion = Mantenciones.objects.get(mantencionID=mantencionID)
    if request.method == 'POST':
        form = MantencionForm(request.POST, instance=mantencion)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mantencion Editada Correctamente!')
            return redirect('registrarMantenciones')
        else:
            messages.error(request, 'Error al editar la mantencion. Por favor, verifica los datos.')
            return render(request, 'edicionMantenciones.html', {'form':form,"mantencionID":mantencionID})
    else:
        form = MantencionForm(instance=mantencion)
        return render(request, 'edicionMantenciones.html', {'form':form,"mantencionID":mantencionID})

def eliminarMantenciones(request,mantencionID):
    mantencion = Mantenciones.objects.get(mantencionID=mantencionID)
    mantencion.delete()
    messages.success(request,'Mantencion Eliminada Correctamente!')
    return redirect('registrarMantenciones')

#EXCEL

from openpyxl import Workbook
from django.http import HttpResponse

def descargar_mantenciones(request):
    mantenciones = Mantenciones.objects.all()
    wb = Workbook()
    ws = wb.active
    # Usar los campos reales del modelo Mantenciones
    ws.append(['ID', 'FechaInicio', 'Duracion', 'Valor', 'Vehiculo'])

    for mantencion in mantenciones:
        vehiculo_text = f"{mantencion.vehiculo.marca} {mantencion.vehiculo.patente}" if mantencion.vehiculo else ''
        ws.append([mantencion.mantencionID, mantencion.fechaInicio, mantencion.duracion, mantencion.valor, vehiculo_text])

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="mantenciones.xlsx"'
    wb.save(response)

    return response