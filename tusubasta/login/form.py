# -*- encoding: utf-8 -*-
from django import forms
from .models import *
from django.db import models
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from django import forms
from django.contrib.auth.models import User

class formRegistrar(forms.Form):
	nickName = forms.CharField(max_length=25, label='Usuario', widget=forms.TextInput(attrs={'class' : 'validate'}))
	email = forms.EmailField(label='Email',max_length=100, widget=forms.EmailInput(attrs={'class' : 'validate'}))
	password = forms.CharField(max_length=25, label='Contraseña', widget=forms.PasswordInput(attrs={'class' : 'validate'}))
	confpassword = forms.password=forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate'}))
	apellido = forms.CharField(max_length=25, label='Apellido', widget=forms.TextInput(attrs={'class' : 'validate'}))
	#fechaNacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class' : 'validate'}))
	nombre = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class' : 'validate'}))


class formLogin(forms.Form):
    username =forms.CharField(label='Usaurio',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Ingrese su usuario','required':''}))
    password = password= forms.password=forms.CharField(max_length=30, label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','required':''}))


class formPerfil(ModelForm):
	fechaNacimiento = forms.DateField(required=False, label = 'Fecha de nacimiento', widget=SelectDateWidget())

	class Meta:
		model 	= Perfil
		fields  = ('direccion', 'direccionNumero', 'ciudad', 'provincia', 'pais', 'fechaNacimiento')
		labels 	= { 'direccion': 'Dirección', 'direccionNumero': 'Número', 'ciudad': 'Ciudad', 'provincia': 'Provincia', 'pais': 'Pais'}

class formUsuario(ModelForm):

	class Meta:
		model 	= User
		fields = ('first_name', 'last_name', 'email')
		labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Dirección de correo'}