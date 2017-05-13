from django.core.exceptions import ValidationError

def titulo_validation(value):
	if not len(value) > 4:
		raise ValidationError('Minimo 4 caracteres')