from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
import os

def upload_to_subastas(intance, filename):
	return os.path.join("Subasta/%s" %intance.titulo+str(datetime.datetime.now()), filename)


# Create your models here.

class Categorias(models.Model):
	descripcion	 		= models.CharField(max_length=50,null=True,blank=False)

	def __str__(self):
		return self.descripcion


class Calificaciones(models.Model):
	descripcion 		= models.CharField(max_length=50,null=True,blank=False)
	fechaAlta			= models.DateTimeField(auto_now=True, null=True,blank=True)
	idUsuarioComprador	= models.ForeignKey(User,null=True,blank=True)

	def __str__(self):
		return self.descripcion


class Subastas(models.Model):
	titulo				= models.CharField(max_length=22,null=True,blank=False)
	detalle 			= models.TextField(null=True,blank=False)
	precioBase 			= models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=False)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaBaja 			= models.DateTimeField(null=True,blank=True)
	fechaFin 			= models.DateField(null=True,blank=True)
	idCategoria 		= models.ForeignKey(Categorias,null=True,blank=True)
	idCalificacion 		= models.ForeignKey(Calificaciones,null=True,blank=True)
	idUsuarioVendedor	= models.ForeignKey(User,null=True,blank=True)
	localidad			= models.CharField(max_length=50,null=True,blank=False)
	provincia			= models.CharField(max_length=50,null=True,blank=False)
	pais				= models.CharField(max_length=50,null=True,blank=False)
	imagenA				= models.ImageField(upload_to=upload_to_subastas, default="", null=True, blank=True)
	imagenB				= models.ImageField(upload_to=upload_to_subastas, default="", null=True, blank=True)
	imagenC				= models.ImageField(upload_to=upload_to_subastas, default="", null=True, blank=True)
	ofertaMax			= models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=False, default=0)
	def __str__(self):
		return self.titulo


class Ofertas(models.Model):
	idSubasta 			= models.ForeignKey(Subastas, null=True, blank=False)
	usuarioComprador 	= models.ForeignKey(User, null=True, blank=False)
	valorOferta 		= models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=False)
	fechaOferta			= models.DateTimeField(auto_now=True, null=True,blank=False)
	ganador 			= models.BooleanField(default=True, null=False)

	def __str__(self):
		return self.valorOferta


class Comentarios(models.Model):
	idSubasta 			= models.ForeignKey(Subastas, null=True, blank=True)
	comentario 			= models.TextField(null=True,blank=False)
	idUsuario			= models.ForeignKey(User,null=True,blank=True)	
	fechaBaja 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)

	def __str__(self):
			return self.comentario

class Respuestas(models.Model):
	idComentario		= models.ForeignKey(Comentarios, null=True, blank=True)
	idUsuario			= models.ForeignKey(User,null=True,blank=True)	
	respuesta			= models.TextField(null=True,blank=True)
	fechaBaja 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)

	def __str__(self):
		return self.respuesta


class Likes(models.Model):
	idSubasta 			= models.ForeignKey(Subastas, null=True, blank=True)
	idUsuarioVendedor	= models.ForeignKey(User,null=True,blank=True)	
	fechaBaja 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)

	def __str__(self):
		return self.fechaAlta


'''
class Imagenes(models.Model):
	idSubasta 			= models.ForeignKey(Subastas)
	descripcion 		= models.CharField(max_length=50,null=True,blank=True)
	URL 				= models.CharField(max_length=150,null=True,blank=True)

	def __str__(self):
		return self.descripcion
'''
