from django import forms
from .models import *
from django.db import models
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from django import forms


class OfertarForm(ModelForm):
	class Meta:
		model 	= Ofertas
		#fields = "__all__"
		fields	= ('valorOferta',)
		labels	= {'valorOferta' : 'Oferta'}


class SubastasForm(ModelForm):
	fechaFin = forms.DateField(required=False, label = 'Fecha de finalización', widget=SelectDateWidget())
 
	class Meta:
		model 	= Subastas
		fields 	= ('titulo', 'detalle', 'precioBase', 'idCategoria','fechaFin', 'localidad', 'provincia', 'pais', 'imagenA', 'imagenB', 'imagenC')
		labels 	= { 'titulo': 'Título', 'detalle': 'Detalle', 'precioBase': 'Precio base', 'idCategoria': 'Categoria', 'fechaFin': 'Fecha finalizacion','localidad' : 'Localidad', 'provincia': 'Provincia', 'pais': 'Pais', 'imagenA': 'Imagen 1', 'imagenB': 'Imagen 2', 'imagenC': 'Imagen 3' }


class ComentariosForm(ModelForm):
	class Meta:
		model	= Comentarios
		fields	= ('comentario',)
		labels	= {'comentario': 'Comentario'}


class RespuestasForm(ModelForm):
	class Meta:
		model 	= Respuestas
		fields 	= ('respuesta',)
		labels 	= {'respuesta': 'Respuesta'}


class DenunciasForm(ModelForm):
	class Meta:
		model 	= Denuncias	
		fields	= ('idMotivo',)
		labels	= {'idMotivo': 'Motivo denuncia'}