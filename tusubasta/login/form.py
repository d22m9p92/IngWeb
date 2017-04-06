from django import forms 
from .models import *

class formRegistro(forms.Form):
	#nickName = form.CharField(max_length=25, label='Usuario',widget=form.TextInput(attrs={'class' : 'validate','requiered'}))
	email = forms.EmailField(label='Email',max_length=100,widget=forms.TextInput(attrs={'class' : 'validate'}))
	#password = forms.password=form.CharField(label='Contraseña', max_length=25,widget=form.PasswordInput((attrs={'class' : 'validate','requiered'})))
	#confpassword = forms.password=forms.CharField(max_length=25, label='Repetir contraseña',widget=forms.PasswordInput(attrs={'class': 'validate','required':''}))
    #nombre = forms.CharField(max_length=30,label='Nombre',widget=forms.TextInput(attrs={'class': 'validate','required':''}))
    #apellido = forms.CharField(max_length=30, label='Apellido',widget=forms.TextInput(attrs={'class': 'validate','required':''}))

		
#Ver Perfil
#Login
#Olvide contraseña
#Cambiar contraseña

