from django.contrib import admin
from .models import Usuario, Encuesta, Eleccion, Voto
# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
	list_display = ('id','mail','name','last',)

class EleccionInline(admin.TabularInline):
	model = Eleccion
	extra = 1

class EncuestaAdmin(admin.ModelAdmin):
	model = Encuesta
	inlines = (EleccionInline,)
	list_display = ('pregunta', 'cuenta_elecciones', 'cuenta_votos_totales')

class VotoAdmin(admin.ModelAdmin):
	model = Voto
	list_display = ('eleccion', 'user', 'encuesta')


admin.site.register(Encuesta, EncuestaAdmin)
admin.site.register(Voto, VotoAdmin)
