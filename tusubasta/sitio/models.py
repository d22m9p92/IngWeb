from django.db import models
from django.contrib.auth.models import User
from django.forms import ModelForm
import datetime
import os

def upload_to_subastas(intance, filename):
	return os.path.join("Subasta/%s" %intance.titulo+str(datetime.datetime.now()), filename)


# Create your models here.

class Categorias(models.Model):
	descripcion	 		= models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.descripcion


class SubCategorias(models.Model):
	descripcion 		= models.CharField(max_length=50,null=True,blank=True)
	idCategoria 		= models.ForeignKey(Categorias,null=True,blank=True)

	def __str__(self):
		return self.descripcion


class Calificaciones(models.Model):
	descripcion 		= models.CharField(max_length=50,null=True,blank=True)
	fechaAlta			= models.DateTimeField(auto_now=True, null=True,blank=True)
	idUsuarioComprador	= models.ForeignKey(User,null=True,blank=True)

	def __str__(self):
		return self.descripcion


class Subastas(models.Model):
	titulo				= models.CharField(max_length=22,null=True,blank=True)
	detalle 			= models.TextField(null=True,blank=True)
	precioBase 			= models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaBaja 			= models.DateTimeField(null=True,blank=True)
	fechaFin 			= models.DateField(null=True,blank=True)
	idCategoria 		= models.ForeignKey(Categorias,null=True,blank=True)
	idSubcategoria 		= models.ForeignKey(SubCategorias,null=True,blank=True)
	idCalificacion 		= models.ForeignKey(Calificaciones,null=True,blank=True)
	#######VERRRR#######
	idUsuarioVendedor	= models.ForeignKey(User,null=True,blank=True)
	localidad			= models.CharField(max_length=50,null=True,blank=True)
	provincia			= models.CharField(max_length=50,null=True,blank=True)
	pais				= models.CharField(max_length=50,null=True,blank=True)
	imagenA				= models.ImageField(upload_to=upload_to_subastas, default="",null=True, blank=True)
	imagenB				= models.ImageField(upload_to=upload_to_subastas, default="", null=True, blank=True)
	imagenC				= models.ImageField(upload_to=upload_to_subastas, default="", null=True, blank=True)

	def __str__(self):
		return self.titulo


class Ofertas(models.Model):
	idSubasta 			= models.ForeignKey(Subastas, null=True, blank=True)
	usuarioComprador 	= models.ForeignKey(User, null=True, blank=True)
	valorOferta 		= models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
	fechaOferta			= models.DateTimeField(auto_now=True, null=True,blank=True)
	ganador 			= models.BooleanField(default=True, null=False)

	def __str__(self):
		return self.valorOferta


class Comentarios(models.Model):
	idSubasta 			= models.ForeignKey(Subastas, null=True, blank=True)
	comentario 			= models.TextField(null=True,blank=True)
	idUsuario			= models.ForeignKey(User,null=True,blank=True)	
	fechaBaja 			= models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaAlta 			= models.DateTimeField(auto_now=True, null=True,blank=True)

	def __str__(self):
			return self.comentario

'''
class Imagenes(models.Model):
	idSubasta 			= models.ForeignKey(Subastas)
	descripcion 		= models.CharField(max_length=50,null=True,blank=True)
	URL 				= models.CharField(max_length=150,null=True,blank=True)

	def __str__(self):
		return self.descripcion
'''

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