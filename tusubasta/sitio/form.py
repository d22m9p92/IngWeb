from django import forms
from .models import *
from django.db import models

class SubastasForm(ModelForm):
	class Meta:
		model = Subastas
		fields = ('titulo', 'detalle', 'precioBase', 'fechaFin', 'idCategoria', 'localidad', 'provincia', 'pais', 'imagen1', 'imagen2', 'imagen3')
		Subastas.fechaFin = widget=forms.DateInput
