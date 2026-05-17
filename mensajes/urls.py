from django.urls import path
from . import views

urlpatterns = [
    path('', views.bandeja_entrada, name='bandeja_entrada'),
    path('enviados/', views.enviados, name='enviados'),
    path('<int:pk>/', views.ver_mensaje, name='ver_mensaje'),
    path('nuevo/', views.nuevo_mensaje, name='nuevo_mensaje'),
]
