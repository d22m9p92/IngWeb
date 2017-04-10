from django import forms
from .models import *

class formRegistrar(forms.Form):
	nickName = forms.CharField(max_length=25, label='Usuario', widget=forms.TextInput(attrs={'class' : 'validate'}))
	email = forms.EmailField(label='Email',max_length=100, widget=forms.TextInput(attrs={'class' : 'validate'}))
	password = forms.CharField(max_length=25, label='Contraseña', widget=forms.PasswordInput(attrs={'class' : 'validate'}))
	confpassword = forms.password=forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate'}))
	apellido = forms.CharField(max_length=25, label='Apellido', widget=forms.TextInput(attrs={'class' : 'validate'}))
	#fechaNacimiento = forms.DateField(label='Fecha de Nacimiento', widget=forms.DateInput(attrs={'class' : 'validate'}))
	nombre = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class' : 'validate'}))
    


class formLogin(forms.Form):
    username =forms.CharField(label='Usaurio',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Ingrese su usuario','required':''}))
    password = password= forms.password=forms.CharField(max_length=30, label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','required':''}))


#Ver Perfil
#Login
#Olvide contraseña
#Cambiar contraseña

