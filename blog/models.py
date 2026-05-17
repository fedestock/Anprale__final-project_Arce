from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=250, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['nombre']


class Articulo(models.Model):
    # Campos requeridos por la consigna:
    # 2 CharField, 1 texto enriquecido, 1 imagen, 1 fecha
    titulo = models.CharField(max_length=200)
    subtitulo = models.CharField(max_length=200, blank=True)
    contenido = RichTextField()  # texto enriquecido con ckeditor
    imagen = models.ImageField(upload_to='articulos/', blank=True, null=True)
    fecha = models.DateField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

    class Meta:
        ordering = ['-fecha']


class Comentario(models.Model):
    articulo = models.ForeignKey(Articulo, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comentario de {self.autor} en {self.articulo}"

    class Meta:
        ordering = ['-fecha']
