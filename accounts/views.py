from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .models import Perfil
from .forms import RegistroForm, EditarUsuarioForm, EditarPerfilForm, CambiarPasswordForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            # Crear perfil vacio para el usuario nuevo
            Perfil.objects.create(usuario=usuario)
            login(request, usuario)
            messages.success(request, f'Bienvenido {usuario.username}!')
            return redirect('home')
    else:
        form = RegistroForm()

    return render(request, 'accounts/registro.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, f'Bienvenido de vuelta, {usuario.username}!')
            return redirect('home')
    else:
        form = AuthenticationForm()
        for field in form.fields.values():
            field.widget.attrs['class'] = 'form-control'

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    messages.info(request, 'Sesión cerrada correctamente.')
    return redirect('home')


@login_required
def perfil(request):
    # Crea el perfil si por alguna razon no existe
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)
    return render(request, 'accounts/perfil.html', {'perfil': perfil})


@login_required
def editar_perfil(request):
    perfil, creado = Perfil.objects.get_or_create(usuario=request.user)

    if request.method == 'POST':
        form_usuario = EditarUsuarioForm(request.POST, instance=request.user)
        form_perfil = EditarPerfilForm(request.POST, request.FILES, instance=perfil)

        if form_usuario.is_valid() and form_perfil.is_valid():
            form_usuario.save()
            form_perfil.save()
            messages.success(request, 'Perfil actualizado correctamente.')
            return redirect('perfil')
    else:
        form_usuario = EditarUsuarioForm(instance=request.user)
        form_perfil = EditarPerfilForm(instance=perfil)

    return render(request, 'accounts/editar_perfil.html', {
        'form_usuario': form_usuario,
        'form_perfil': form_perfil,
    })


@login_required
def cambiar_password(request):
    if request.method == 'POST':
        form = CambiarPasswordForm(request.user, request.POST)
        if form.is_valid():
            usuario = form.save()
            update_session_auth_hash(request, usuario)
            messages.success(request, 'Contraseña cambiada correctamente.')
            return redirect('perfil')
    else:
        form = CambiarPasswordForm(request.user)

    return render(request, 'accounts/cambiar_password.html', {'form': form})
