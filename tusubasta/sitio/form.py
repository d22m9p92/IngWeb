from django import forms
from .models import *
from django.db import models

class SubastasForm(ModelForm):
	fechaFin = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
	# imagen1 = forms.ImageField(upload_to=upload_to_subastas, default="")	

	class Meta:
		model = Subastas
		fields = ('titulo', 'detalle', 'precioBase', 'idCategoria', 'fechaFin', 'localidad', 'provincia', 'pais', 'imagenA', 'imagenB', 'imagenC')
		labels = { 'titulo': 'Título', 'detalle': 'Detalle', 'precioBase': 'Precio base', 'idCategoria': 'Categoria', 'localidad' : 'Localidad', 'provincia': 'Provincia', 'pais': 'Pais', 'imagenA': 'Imagen 1', 'imagenB': 'Imagen 2', 'imagenC': 'Imagen 3' }
