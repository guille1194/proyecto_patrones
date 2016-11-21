from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.urlresolvers import reverse
from django.core.validators import MaxValueValidator, MinValueValidator,MaxValueValidator
from django.utils import timezone
import datetime
import time

# Create your models here.

class QuerySet(models.QuerySet):

	def get_categoria(self):
		return self.nombre

class Usuario(models.Model):
	ID_Usuario = models.AutoField(primary_key=True)
	user_perfil = models.OneToOneField(User, related_name="profile")
	email = models.EmailField()
	name = models.CharField(max_length=64)
	last = models.CharField(max_length=64)

	def __unicode__(self):
		return '%s'%(self.id)

class Categoria(models.Model):
	ID_Categoria = models.AutoField(primary_key=True)
	num_cat = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=100)

	def _unicode_(self):
		return 'Categoria %d: %s' %(self.num_cat, self.nombre)

class Encuesta(models.Model):
	ID_Encuesta = models.AutoField(primary_key=True)
	titulo = models.CharField(max_length=64)
	categoria = models.CharField(max_length=64)
	fecha_creacion = models.DateField(default=datetime.date.today)
	publicado = models.BooleanFueld(default=True)
	propietario = models.ForeignKey(Usuario,related_name='usuarion',null=True,blank=True,)

	class Meta:
		ordering = ['-fecha_creacion']


	def contar_votos(self):
		return self.set_eleccion.count()

	def contar_votos_totales(self):
		resultado = 0
		for eleccion in self.set_eleccion.all():
			resultado += eleccion.contar_votos()
		return resultado

	def puede_votar(self,Usuario):
		return not self.set_voto.filter(user=Usuario).exists()

	def __unicode__(self):
		return '%s'%(self.id)

class Eleccion(models.Model):
	ID_Eleccion = models.AutoField(primary_key=True)
	encuesta = models.ForeignKey(Encuesta)
	ELECCION = (
		('SI', 'Si'),
		('NO', 'No'),
	)
	eleccion = models.CharField(max_length=1, choices=ELECCION)

	def contar_votos(self):
		return self.set_voto.count()

	def _unicode_(self):
		return self.eleccion

class Voto(models.Model):
	ID_Voto = models.AutoField(primary_key=True)
	usuario = models.ForeignKey(Usuario)
	encuesta = models.ForeignKey(Encuesta)
	eleccion = models.ForeignKey(Eleccion)

	def _unicode_(self):
		return u'Voto para %s' % (self.eleccion)

	class Meta:
		unique_together = ('usuario', 'encuesta')
