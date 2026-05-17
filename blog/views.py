from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.db.models import Q
from .models import Articulo, Categoria, Comentario
from .forms import ArticuloForm, CategoriaForm, ComentarioForm, BuscadorForm


# Vista de inicio
def home(request):
    articulos = Articulo.objects.filter(publicado=True)
    categorias = Categoria.objects.all()
    form = BuscadorForm(request.GET)

    if form.is_valid() and form.cleaned_data['busqueda']:
        termino = form.cleaned_data['busqueda']
        articulos = articulos.filter(
            Q(titulo__icontains=termino) |
            Q(subtitulo__icontains=termino)
        )

    return render(request, 'blog/home.html', {
        'articulos': articulos,
        'categorias': categorias,
        'form': form,
    })


# Vista about / acerca de
def about(request):
    return render(request, 'blog/about.html')


# Lista de articulos (route pages/)
def lista_articulos(request):
    articulos = Articulo.objects.filter(publicado=True)
    form = BuscadorForm(request.GET)

    if form.is_valid() and form.cleaned_data['busqueda']:
        termino = form.cleaned_data['busqueda']
        articulos = articulos.filter(
            Q(titulo__icontains=termino) |
            Q(subtitulo__icontains=termino)
        )

    return render(request, 'blog/lista_articulos.html', {
        'articulos': articulos,
        'form': form,
    })


# Detalle de un articulo
def detalle_articulo(request, pk):
    articulo = get_object_or_404(Articulo, pk=pk)
    comentarios = articulo.comentarios.all()
    form_comentario = ComentarioForm()

    if request.method == 'POST':
        if not request.user.is_authenticated:
            messages.error(request, 'Debes iniciar sesión para comentar.')
            return redirect('login')
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            comentario = form_comentario.save(commit=False)
            comentario.articulo = articulo
            comentario.autor = request.user
            comentario.save()
            messages.success(request, 'Comentario agregado.')
            return redirect('detalle_articulo', pk=pk)

    return render(request, 'blog/detalle_articulo.html', {
        'articulo': articulo,
        'comentarios': comentarios,
        'form_comentario': form_comentario,
    })


# Crear articulo - requiere login (decorador)
@login_required
def crear_articulo(request):
    if request.method == 'POST':
        form = ArticuloForm(request.POST, request.FILES)
        if form.is_valid():
            articulo = form.save(commit=False)
            articulo.autor = request.user
            articulo.save()
            messages.success(request, 'Artículo creado correctamente.')
            return redirect('detalle_articulo', pk=articulo.pk)
    else:
        form = ArticuloForm()

    return render(request, 'blog/form_articulo.html', {
        'form': form,
        'titulo_form': 'Nuevo artículo',
    })


# Editar articulo - CBV con LoginRequiredMixin (mixin requerido por la consigna)
class EditarArticulo(LoginRequiredMixin, UpdateView):
    model = Articulo
    form_class = ArticuloForm
    template_name = 'blog/form_articulo.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo_form'] = 'Editar artículo'
        return context

    def get_success_url(self):
        return reverse_lazy('detalle_articulo', kwargs={'pk': self.object.pk})


# Borrar articulo - CBV con LoginRequiredMixin
class BorrarArticulo(LoginRequiredMixin, DeleteView):
    model = Articulo
    template_name = 'blog/confirmar_borrado.html'
    success_url = reverse_lazy('lista_articulos')


# Crear categoria - requiere login (decorador)
@login_required
def crear_categoria(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada correctamente.')
            return redirect('lista_articulos')
    else:
        form = CategoriaForm()

    return render(request, 'blog/form_categoria.html', {'form': form})


# Articulos por categoria
def articulos_por_categoria(request, pk):
    categoria = get_object_or_404(Categoria, pk=pk)
    articulos = Articulo.objects.filter(categoria=categoria, publicado=True)

    return render(request, 'blog/articulos_por_categoria.html', {
        'categoria': categoria,
        'articulos': articulos,
    })
