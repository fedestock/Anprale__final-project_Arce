# Anprale — Blog de Refugios de Montaña 🏔️

Proyecto final del curso **Arce**. Aplicación web desarrollada con **Django** que funciona como blog sobre los refugios de montaña en El Bolsón, Patagonia, Argentina.

---

## ✨ Funcionalidades

- Listado y detalle de artículos con texto enriquecido (CKEditor)
- Búsqueda de artículos por título o subtítulo
- Filtrado de artículos por categoría
- Sistema de comentarios (requiere inicio de sesión)
- Registro, inicio y cierre de sesión de usuarios
- Perfil de usuario con avatar, biografía y ubicación
- Sistema de mensajes privados entre usuarios
- Panel de administración de Django

---

## 🗂️ Estructura del proyecto

```
Anprale__final-project_Arce/
├── anprale_project/       # Configuración principal (settings, urls, wsgi)
├── blog/                  # App principal: artículos, categorías, comentarios
├── accounts/              # App de usuarios: registro, perfil
├── mensajes/              # App de mensajes privados
├── templates/             # Templates HTML globales
├── manage.py
└── requirements.txt
```

---

## 🛠️ Tecnologías

- Python 3.10+
- Django 4.2
- django-ckeditor (editor de texto enriquecido)
- Pillow (manejo de imágenes)
- SQLite (base de datos por defecto)

---

## 🚀 Instalación y puesta en marcha

### 1. Clonar el repositorio

```bash
git clone https://github.com/fedestock/Anprale__final-project_Arce.git
cd Anprale__final-project_Arce
```

### 2. Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate        # Linux / macOS
venv\Scripts\activate           # Windows
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Crear un superusuario (opcional, para acceder al admin)

```bash
python manage.py createsuperuser
```

### 6. Ejecutar el servidor de desarrollo

```bash
python manage.py runserver
```

Abrí el navegador en [http://127.0.0.1:8000](http://127.0.0.1:8000).

---

## ⚙️ Configuración relevante

| Variable | Valor por defecto |
|---|---|
| `LANGUAGE_CODE` | `es-es` |
| `TIME_ZONE` | `America/Argentina/Buenos_Aires` |
| `DEBUG` | `True` |
| `DATABASE` | SQLite (`db.sqlite3`) |
| `MEDIA_ROOT` | `media/` |
| `STATIC_ROOT` | `staticfiles/` |

> ⚠️ Para producción, asegurate de cambiar `SECRET_KEY`, establecer `DEBUG = False` y configurar `ALLOWED_HOSTS` correctamente.

---

## 👤 Autor

Desarrollado por **Arce** como proyecto final del curso.

Temática: refugios de montaña en **El Bolsón, Patagonia, Argentina** 🇦🇷
