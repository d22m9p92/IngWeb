from django import forms
from .models import *
from django.db import models

class SubastasForm(ModelForm):
	fechaFin = forms.DateField(widget=forms.SelectDateWidget())
	# forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}))
	

	class Meta:
		model = Subastas
		fields = ('titulo', 'detalle', 'precioBase', 'idCategoria', 'localidad', 'provincia', 'pais', 'imagen1', 'imagen2', 'imagen3')
		#widgets = { 'fechaFin': forms.DateInput(attrs={'class':'datepicker'})}
		labels = { 'titulo': 'Título', 'detalle': 'Detalle', 'precioBase': 'Precio base', 'idCategoria': 'Categoria', 'localidad' : 'Localidad', 'provincia': 'Provincia', 'pais': 'Pais', 'imagen1': 'Imagen 1', 'imagen2': 'Imagen 2', 'imagen3': 'Imagen 3' }
