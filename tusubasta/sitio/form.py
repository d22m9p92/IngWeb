from django import forms
from .models import *
from django.db import models
from django.forms import ModelForm
#from .validaciones import titulo_validation


class OfertarForm(ModelForm):
	class Meta:
		model 	= Ofertas
		#fields = "__all__"
		fields	= ('valorOferta',)
		labels	= {'valorOferta' : 'Oferta'}



class SubastasForm(ModelForm):
	fechaFin = forms.DateField(required=False, label = 'Fecha de finalización', widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))

#	def __init__(self):
#		super().__init__()
		#self.fields['titulo'].validaciones.append(titulo_validation)

	class Meta:
		model 	= Subastas
		fields 	= ('titulo', 'detalle', 'precioBase', 'idCategoria', 'fechaFin', 'localidad', 'provincia', 'pais', 'imagenA', 'imagenB', 'imagenC')
		labels 	= { 'titulo': 'Título', 'detalle': 'Detalle', 'precioBase': 'Precio base', 'idCategoria': 'Categoria', 'localidad' : 'Localidad', 'provincia': 'Provincia', 'pais': 'Pais', 'imagenA': 'Imagen 1', 'imagenB': 'Imagen 2', 'imagenC': 'Imagen 3' }



'''
class Comentarios(ModelForm):
	class Meta:
		model 	= Comentarios
		fields 	= ('comentario')
		labels 	= ('Comentario')
'''
'''
class Respuestas(ModelForm):
	class Meta:
		model 	= Respuestas
		fields 	= ('respuesta')
		labels 	= ('Comentario')
'''