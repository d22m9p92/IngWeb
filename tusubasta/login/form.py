from django import forms 
from .models import *

class formRegistro(forms.Form):
	nickName = forms.CharField(max_length=25, label='Usuario', widget=forms.TextInput(attrs={'class' : 'validate'}))
	email = forms.EmailField(label='Email',max_length=100, widget=forms.TextInput(attrs={'class' : 'validate'}))
	#password = forms.password=form.CharField(label='Contraseña', max_length=25, widget=forms.PasswordInput((attrs={'class' : 'validate'}))
	password = forms.CharField(max_length=25, label='Usuario', widget=forms.PasswordInput(attrs={'class' : 'validate'}))
	confpassword = forms.password=forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate'}))
	nombre = forms.CharField(max_length=25, label='Nombre', widget=forms.TextInput(attrs={'class' : 'validate'}))
    #apellido = forms.CharField(max_length=25, label='Apellido', widget=forms.TextInput(attrs={'class' : 'validate'}))


class formLogin(forms.Form):
    email =forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class' : 'form-control','placeholder':'Ingrese su email','required':''})) 
    password = password= forms.password=forms.CharField(max_length=30, label='Password',widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder':'Ingrese su clave','required':''}))


		
#Ver Perfil
#Login
#Olvide contraseña
#Cambiar contraseña

