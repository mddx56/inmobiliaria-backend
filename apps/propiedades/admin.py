from django.contrib import admin

from .models import (
    Area,
    Caracteristica,
    Casa,
    Ciudad,
    Departamento,
    Imagen,
    Punto,
    Terreno,
    TipoInmueble,
    Zona,
)

admin.site.site_header = "Inmuebles"
admin.site.site_title = "Casas"
admin.site.index_title = "Bienvenidos 🤠"

# Register your models here.
admin.site.register(Area)
admin.site.register(Caracteristica)
admin.site.register(Casa)
admin.site.register(Ciudad)
admin.site.register(Departamento)
admin.site.register(Imagen)
# admin.site.register(Inmueble)
admin.site.register(Punto)
admin.site.register(Terreno)
admin.site.register(TipoInmueble)
admin.site.register(Zona)
