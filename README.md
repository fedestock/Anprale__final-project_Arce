# Anprale Refugios - Blog de Montaña

Blog sobre los refugios de la cadena Anprale en El Bolsón, Patagonia Argentina.
Proyecto final de Python en CoderHouse.

## Instalación

```
python -m venv venv
venv\Scripts\activate        (Windows)
source venv/bin/activate     (Mac/Linux)
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Abrir en: http://localhost:8000

## Funcionalidades

- Home con listado de artículos y buscador
- About / Acerca de (route /about/)
- Pages / Artículos (route /pages/)
- Detalle de artículo con comentarios
- Crear, editar y borrar artículos (requiere login)
- Registro, login y logout de usuarios
- Perfil de usuario con avatar y biografía
- Edición de perfil y cambio de contraseña
- Sistema de mensajería entre usuarios
- Panel de administración en /admin/

## Orden de prueba

1. Crear superusuario: python manage.py createsuperuser
2. Ir a /admin/ y crear algunas categorías
3. Ir al home y registrar un usuario
4. Crear artículos desde el navbar
5. Comentar artículos
6. Editar perfil desde el menú de usuario
7. Enviar un mensaje a otro usuario desde /mensajes/nuevo/

## Requisitos cumplidos

- Herencia de templates (base.html)
- 2 CBV: EditarArticulo y BorrarArticulo (con LoginRequiredMixin)
- 1 decorador: @login_required en crear_articulo, crear_categoria y vistas de mensajes
- Vista home, about, pages, detalle
- Modelo Articulo con 2 CharField, RichTextField, ImageField, DateField
- Buscador con mensaje si no hay resultados
- Login, logout, registro
- Perfil con nombre, apellido, email, avatar, biografia
- App accounts separada
- App mensajes separada
- Todos los modelos en admin
- .gitignore con __pycache__, db.sqlite3, media
- requirements.txt actualizado
