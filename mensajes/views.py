from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Mensaje
from .forms import MensajeForm


@login_required
def bandeja_entrada(request):
    mensajes_recibidos = Mensaje.objects.filter(destinatario=request.user)
    return render(request, 'mensajes/bandeja.html', {'mensajes': mensajes_recibidos})


@login_required
def enviados(request):
    mensajes_enviados = Mensaje.objects.filter(remitente=request.user)
    return render(request, 'mensajes/enviados.html', {'mensajes': mensajes_enviados})


@login_required
def ver_mensaje(request, pk):
    mensaje = get_object_or_404(Mensaje, pk=pk)
    # Marcar como leido si soy el destinatario
    if mensaje.destinatario == request.user and not mensaje.leido:
        mensaje.leido = True
        mensaje.save()
    return render(request, 'mensajes/ver_mensaje.html', {'mensaje': mensaje})


@login_required
def nuevo_mensaje(request):
    if request.method == 'POST':
        form = MensajeForm(request.POST)
        if form.is_valid():
            mensaje = form.save(commit=False)
            mensaje.remitente = request.user
            mensaje.save()
            messages.success(request, 'Mensaje enviado correctamente.')
            return redirect('bandeja_entrada')
    else:
        form = MensajeForm()

    return render(request, 'mensajes/nuevo_mensaje.html', {'form': form})
