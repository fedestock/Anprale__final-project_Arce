from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('pages/', views.lista_articulos, name='lista_articulos'),
    path('pages/<int:pk>/', views.detalle_articulo, name='detalle_articulo'),
    path('pages/nuevo/', views.crear_articulo, name='crear_articulo'),
    path('pages/<int:pk>/editar/', views.EditarArticulo.as_view(), name='editar_articulo'),
    path('pages/<int:pk>/borrar/', views.BorrarArticulo.as_view(), name='borrar_articulo'),
    path('categoria/nueva/', views.crear_categoria, name='crear_categoria'),
    path('categoria/<int:pk>/', views.articulos_por_categoria, name='articulos_por_categoria'),
]
