from django import forms
from .models import *
from django.db import models

class SubastasForm(ModelForm):
	class Meta:
		model = Subastas
		fields = "__all__"

'''
class formSubasta(forms.Form):
	detalle 			= forms.TextField(max_length =500, label = 'Detalle', widget=forms.TextInput(attrs={'class' : 'validate'}))
	precioBase 			= forms.DecimalField(max_digits=7, decimal_places=2, label = 'Precio Base', widget=forms.TextInput(attrs={'class' : 'validate'}))
	fechaFin 			= forms.DateField(label='Fecha Finalizacion', widget=forms.DateInput(attrs={'class' : 'validate'}))
	usuarioVendedor 	= forms.ForeignKey(Categorias,null=True,blank=True)
	idCategoria			= forms.ModelMultipleChoiceField(queryset = Categorias.objects.all(), label = 'Categoria', widget = forms.TextInput(attrs={'class' : 'validate'}))
	idSubcategoria 		= forms.ModelMultipleChoiceField(queryset = SubCategorias.objects., label = 'Categoria', widget = forms.TextInput(attrs={'class' : 'validate'}))
	localidad			= forms.CharField(max_length=25, label = 'Usuario', widget=forms.TextInput(attrs={'class' : 'validate'}))
	imagen1				= froms.ImageField(label = 'Imagen N°1')
	imagen2				= froms.ImageField(label = 'Imagen N°2')
	imagen3				= froms.ImageField(label = 'Imagen N°3')

class formRegistrar(forms.Form):
	nickName = forms.CharField(max_length=25, label='Usuario', widget=forms.TextInput(attrs={'class' : 'validate'}))
	email = forms.EmailField(label='Email',max_length=100, widget=forms.TextInput(attrs={'class' : 'validate'}))
	password = forms.CharField(max_length=25, label='Contraseña', widget=forms.PasswordInput(attrs={'class' : 'validate'}))
	confpassword = forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate'}))
	apellido = forms.CharField(max_length=25, label='Apellido', widget=forms.TextInput(attrs={'class' : 'validate'}))
	fechaNacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class' : 'validate'}))
	nombre = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class' : 'validate'}))
    
    #nombre2 = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class' : 'validate'}))
    
#forms.password=f

class formLogin(forms.Form):
    username =forms.CharField(label='Usaurio',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Ingrese su usuario','required':''}))
    password = password= forms.password=forms.CharField(max_length=30, label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','required':''}))

'''
#Ver Perfil
#Login
#Olvide contraseña
#Cambiar contraseña

