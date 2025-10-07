from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Recorridos
from .forms import RecorridosForm
from django.contrib.auth.decorators import login_required


# Simulación de precios de bencina en tiempo real
PRECIOS_BENCINA = {
    '93': 1350,
    '95': 1400,
    '97': 1450,
    'diesel': 1200,
}
def obtener_precio_bencina(tipo_bencina):
    return PRECIOS_BENCINA.get(tipo_bencina, 1400)

@login_required
def registrarRecorridos(request):
    recorridos = Recorridos.objects.all()
    gasto_bencina = None
    precio_bencina = None
    if request.method == 'POST':
        form = RecorridosForm(request.POST)
        if form.is_valid():
            recorrido = form.save(commit=False)
            vehiculo = recorrido.vehiculo
            tipo_bencina = getattr(vehiculo, 'tipo_bencina', '93')
            rendimiento = getattr(vehiculo, 'rendimiento', 10)
            distancia = recorrido.distancia_km or 0
            precio_bencina = obtener_precio_bencina(tipo_bencina)
            if distancia > 0 and rendimiento > 0:
                gasto_bencina = round((distancia / rendimiento) * precio_bencina, 2)
            recorrido.save()
            messages.success(request, f'Recorrido Registrado Correctamente! Gasto estimado de bencina: ${gasto_bencina if gasto_bencina else "N/A"}')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al registrar el recorrido. Por favor, verificar los datos.')
            return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos, "gasto_bencina":gasto_bencina, "precio_bencina":precio_bencina})
    else:
        form = RecorridosForm()
        return render(request,'gestionRecorrido.html', {"form":form, "recorridos":recorridos, "gasto_bencina":gasto_bencina, "precio_bencina":precio_bencina})

def editarRecorridos(request, recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    if request.method == 'POST':
        form = RecorridosForm(request.POST, instance=recorrido)
        if form.is_valid():
            form.save()
            messages.success(request, 'Recorrido Editado Correctamente!')
            return redirect('registrarRecorridos')
        else:
            messages.error(request, 'Error al editar el recorrido. Por favor, verifica los datos.')
            return render(request, 'edicionRecorrido.html', {'form':form,"recorridoID":recorridoID})
    else:
        form = RecorridosForm(instance=recorrido)
        return render(request, 'edicionRecorrido.html', {'form':form,"recorridoID":recorridoID})

def eliminarRecorridos(request,recorridoID):
    recorrido = Recorridos.objects.get(recorridoID=recorridoID)
    recorrido.delete()
    messages.success(request,'Recorrido Eliminado Correctamente!')
    return redirect('registrarRecorridos')

  
#Excel
from openpyxl import Workbook
from django.http import HttpResponse

def descargarRecorridos(request):
    recorridos = Recorridos.objects.all()
    wb = Workbook()
    ws = wb.active
    ws.append(['recorridoID', 'conductor', 'vehiculo.', 'fecha', 'direccionOrigen', 'direccionDestino', 'carga', 'detalle'])

    for recorrido in recorridos:
        ws.append([recorrido.recorridoID, recorrido.conductor.nombre, recorrido.vehiculo.patente, recorrido.fecha, recorrido.direccionOrigen, recorrido.direccionDestino, recorrido.carga, recorrido.detalle])
    
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename="recorridos.xlsx"'
    wb.save(response)

    return response

def detalleRecorrido(request, recorridoID):
    recorrido = get_object_or_404(Recorridos, recorridoID=recorridoID)
    return render(request, 'detalleRecorrido.html', {'recorrido': recorrido})

def detalleGastoBencina(request, recorridoID):
    from .views import PRECIOS_BENCINA, obtener_precio_bencina
    from .models import Recorridos
    recorrido = get_object_or_404(Recorridos, recorridoID=recorridoID)
    vehiculo = recorrido.vehiculo
    tipo_bencina = getattr(vehiculo, 'tipo_bencina', '93')
    rendimiento = getattr(vehiculo, 'rendimiento', 10)
    distancia = recorrido.distancia_km or 0
    precio_bencina = obtener_precio_bencina(tipo_bencina)
    gasto_bencina = None
    if distancia > 0 and rendimiento > 0:
        gasto_bencina = round((distancia / rendimiento) * precio_bencina, 2)
    return render(request, 'detalleGastoBencina.html', {
        'recorrido': recorrido,
        'precio_bencina': precio_bencina,
        'gasto_bencina': gasto_bencina,
        'precios_bencina': PRECIOS_BENCINA
    })