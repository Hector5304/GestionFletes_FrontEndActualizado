from django.shortcuts import render, redirect
from .forms import RegistroUsuarioForm
from django.contrib import messages

# Create your views here.
def regitro(request):
    if request.method == 'POST':
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            nombre = form.cleaned_data['username']
            messages.success(request, f'Usuario {nombre} creado')
            return redirect('login')
    else:
        form = RegistroUsuarioForm()
        messages.error(request, 'Error al crear usuario')
    context = {'form': form}

    return render(request, 'registro.html', context)

def login_view(request):
    #código de inicio de sesión 
    messages.success(request, 'Has iniciado sesión correctamente.')
    return redirect('home')

def logout_view(request):
    #código de cierre de sesión 
    messages.success(request, 'Has cerrado sesión correctamente.')
    return redirect('login')