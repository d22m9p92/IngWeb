# -*- encoding: utf-8 -*-
from django import forms
from .models import *
from django.db import models
from django.forms import ModelForm
from django.forms.extras import SelectDateWidget
from django import forms
from django.contrib.auth.models import User

YearNacimiento = [1930, 1931, 1932, 1933, 1934, 1935, 1936, 1937, 1938, 
1939, 1940, 1941, 1942, 1943, 1944, 1945, 1946, 1947, 1948, 1949, 1950, 
1951, 1952, 1953, 1954, 1955, 1956, 1957, 1958, 1959, 1960, 1961, 1962, 
1963, 1964, 1965, 1966, 1967, 1968, 1969, 1970, 1971, 1972, 1973, 1974, 
1975, 1976, 1977, 1978, 1979, 1980, 1981, 1982, 1983, 1984, 1985, 1986, 
1987, 1988, 1989, 1990, 1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 
1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]

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
	fechaNacimiento = forms.DateField(required=False, label = 'Fecha de nacimiento', widget=SelectDateWidget(years = YearNacimiento))

	class Meta:
		model 	= Perfil
		fields  = ('direccion', 'direccionNumero', 'ciudad', 'provincia', 'pais', 'fechaNacimiento')
		labels 	= { 'direccion': 'Dirección', 'direccionNumero': 'Número', 'ciudad': 'Ciudad', 'provincia': 'Provincia', 'pais': 'Pais'}


class formUsuario(ModelForm):

	class Meta:
		model 	= User
		fields = ('first_name', 'last_name', 'email')
		labels = {'first_name': 'Nombre', 'last_name': 'Apellido', 'email': 'Dirección de correo'}


class OlvidoContraseña(forms.Form):
	email = forms.EmailField(label='Email',max_length=100, widget=forms.EmailInput(attrs={'class' : 'validate'}))


class renovarContraseña(forms.Form):
	password = forms.CharField(max_length=25, label='Contraseña', widget=forms.PasswordInput(attrs={'class' : 'validate'}))
	confpassword = forms.password=forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate'}))