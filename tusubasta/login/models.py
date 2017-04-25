# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from sitio.models import *

# class estadosPerfil(models.Model):
# descripcion = models.CharField(max_length=50, null=True,blank=True)
'''
class Usuarios(AbstractBaseUser):
	
	nick = models.CharField(max_length=50, null=True, blank=True)
	direccion = models.CharField(max_length=50, null=True, blank=True)
	direccionNumero = models.IntegerField(default=0)
	#ciudad = models.ForeignKey(null=True,blank= True)
	fechaNacimiento = models.DateField(null=True, blank=True)	

		objects = MyUserManager()

	def __str__(self):
			return self.nick

'''
class EstadosUsuarios(models.Model):
	descripcion			= models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.descripcion


class TiposUsuarios(models.Model):
	descripcion			=  models.CharField(max_length=50, null=True, blank=True)

	def __str__(self):
		return self.descripcion


class Perfil(models.Model):
	direccion 			= models.CharField(max_length=50, null=True, blank=True)
	direccionNumero 	= models.IntegerField(default=0)
	ciudad				= models.CharField(max_length=50, null=True, blank=True)
	provincia			= models.CharField(max_length=50, null=True, blank=True)
	pais				= models.CharField(max_length=50, null=True, blank=True)
	fechaNacimiento 	= models.DateField(null=True, blank=True)
	# estado = models.ForeignKey(estadosPerfil)
	usuario 			= models.OneToOneField(User,on_delete = models.CASCADE, null=True, blank=True)
	idEstadoUsuario		= models.ForeignKey(EstadosUsuarios, null=True, blank=True)
	idTipoUsuario		= models.ForeignKey(TiposUsuarios, null=True, blank=True)

	def __str__(self):
		return self.usuario