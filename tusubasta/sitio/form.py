from django import forms
from .models import *
from django.db import models

class SubastasForm(ModelForm):
	fechaFin = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control datepicker'}))
	# imagen1 = forms.ImageField(upload_to=upload_to_subastas, default="")	

	class Meta:
		model = Subastas
		fields = ('titulo', 'detalle', 'precioBase', 'idCategoria', 'fechaFin', 'localidad', 'provincia', 'pais', 'imagenA', 'imagenB', 'imagenC')
		labels = { 'titulo': 'Título', 'detalle': 'Detalle', 'precioBase': 'Precio base', 'idCategoria': 'Categoria', 'localidad' : 'Localidad', 'provincia': 'Provincia', 'pais': 'Pais', 'imagen1': 'Imagen 1', 'imagen2': 'Imagen 2', 'imagen3': 'Imagen 3' }