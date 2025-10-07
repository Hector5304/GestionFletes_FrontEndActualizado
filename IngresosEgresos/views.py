from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Ingresos, Egresos
from .forms import IngresosForm, EgresosForm

@login_required
def registrarIngresos(request):
    ingresos = Ingresos.objects.all()
    if request.method == 'POST':
        form = IngresosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingreso Registrado Correctamente!')
            return redirect('registrarIngresos')
        else:
            messages.error(request, 'Error al registrar el ingreso. Por favor, verificar los datos.')
            return render(request,'gestionIngresos.html', {"form":form, "ingresos":ingresos})
    else:
        form = IngresosForm()
        return render(request,'gestionIngresos.html', {"form":form, "ingresos":ingresos})

def editarIngresos(request, ingresoID):
    ingreso = Ingresos.objects.get(ingresoID=ingresoID)
    if request.method == 'POST':
        form = IngresosForm(request.POST, instance=ingreso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Ingreso Editado Correctamente!')
            return redirect('registrarIngresos')
        else:
            messages.error(request, 'Error al editar el Ingreso. Por favor, verifica los datos.')
            return render(request, 'edicionIngresos.html', {'form':form,"ingresoID":ingresoID})
    else:
        form = IngresosForm(instance=ingreso)
        return render(request, 'edicionIngresos.html', {'form':form,"ingresoID":ingresoID})

def eliminarIngresos(request,ingresoID):
    ingreso = Ingresos.objects.get(ingresoID=ingresoID)
    ingreso.delete()
    messages.success(request,'Ingreso Eliminado Correctamente!')
    return redirect('registrarIngresos')

# Egresos

def registrarEgresos(request):
    egresos = Egresos.objects.all()
    if request.method == 'POST':
        form = EgresosForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Egreso Registrado Correctamente!')
            return redirect('registrarEgresos')
        else:
            messages.error(request, 'Error al registrar el Egreso. Por favor, verificar los datos.')
            return render(request,'gestionEgresos.html', {"form":form, "egresos":egresos})
    else:
        form = EgresosForm()
        return render(request,'gestionEgresos.html', {"form":form, "egresos":egresos})

def editarEgresos(request, egresoID):
    egreso = Egresos.objects.get(egresoID=egresoID)
    if request.method == 'POST':
        form = EgresosForm(request.POST, instance=egreso)
        if form.is_valid():
            form.save()
            messages.success(request, 'Egreso Editado Correctamente!')
            return redirect('registrarEgresos')
        else:
            messages.error(request, 'Error al editar el Egreso. Por favor, verifica los datos.')
            return render(request, 'edicionEgresos.html', {'form':form,"egresoID":egresoID})
    else:
        form = EgresosForm(instance=egreso)
        return render(request, 'edicionEgresos.html', {'form':form,"egresoID":egresoID})

def eliminarEgresos(request, egresoID):
    egreso = Egresos.objects.get(egresoID=egresoID)
    egreso.delete()
    messages.success(request,'Egreso Eliminado Correctamente!')
    return redirect('registrarEgresos')