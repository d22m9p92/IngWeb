from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.

class categoria(models.Model):
	descripcion = models.CharField(max_length=50,null=True,blank=True)

class subCategoria(models.Model):
	descripcion = models.CharField(max_length=50,null=True,blank=True)
	idCategoria = models.ForeignKey(categoria)

class calificacion(models.Model):
	descripcion = models.CharField(max_length=50,null=True,blank=True)

class cabSubasta(models.Model):
	descripcion = models.TextField(null=True,blank=True)
	precioBase = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
	fechaAlta = models.DateTimeField(auto_now=True, null=True,blank=True)
	fechaBaja = models.DateTimeField(auto_now=True, null=True,blank=True)
	usuarioVendedor = models.OneToOneField(User)
	imagen = models.ImageField(null=True,blank=True) #upload_to='photo'
	idSubcategoria = models.ForeignKey(subCategoria)
	idCalificacion = models.ForeignKey(calificacion)

class detSubasta(models.Model):
	idSubasta = models.ForeignKey(cabSubasta)
	usuarioComprador = models.ForeignKey(User)
	valorOferta = models.DecimalField(max_digits=7, decimal_places=2,null=True,blank=True)
	fechaOferta = models.DateTimeField(auto_now=True, null=True,blank=True)
	estado = models.BooleanField(default=True, null=False)


