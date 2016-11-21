from django.contrib import admin
from .models import Usuario, Encuesta, Eleccion, Voto, Categoria
# Register your models here.

admin.site.register(Encuesta)
admin.site.register(Voto)
admin.site.register(Usuario)
admin.site.register(Eleccion)
admin.site.register(Categoria)
