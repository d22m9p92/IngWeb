# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from sitio.models import *

# class estadosPerfil(models.Model):
# descripcion = models.CharField(max_length=50, null=True,blank=True)


class perfil(models.Model):
	nick = models.CharField(max_length=50, null=True, blank=True)
	direccion = models.CharField(max_length=50, null=True, blank=True)
	direccionNumero = models.IntegerField(default=0)
	# ciudad = models.ForeignKey(null=True,blank= True)
	fechaNacimiento = models.DateField(null=True, blank=True)
	# estado = models.ForeignKey(estadosPerfil)
	usuario = models.ForeignKey(User)

	def __str__(self):
		return self.nick




