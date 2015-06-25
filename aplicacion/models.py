from django.db import models
from django.contrib.auth.models import User

class Categoria(models.Model):
	nombre = models.CharField(max_length= 50)
	descripcion = models.CharField(max_length= 200)

class Usuario(models.Model):
	fNacimiento = models.DateField()
	sexo = models.BooleanField()
	telefono = models.CharField(max_length = 20)
	#user = models.ForeignKey(User)

class Publicacion(models.Model):
	nombre = models.CharField(max_length=100)
	fechaInicio = models.DateField()
	fechaCierre = models.DateField()
	usuario = models.ForeignKey(Usuario)
	categoria = models.ForeignKey(Categoria)
	descripcion = models.CharField(max_length = 300)

class Postulante(models.Model):
	usuario = models.ForeignKey(Usuario)
	publicacion = models.ForeignKey(Publicacion)

class Calificacion(models.Model):
	calificacion = models.IntegerField()
	tipo = models.BooleanField()
	usuario = models.ForeignKey(Usuario)
	publicacion = models.ForeignKey(Publicacion)