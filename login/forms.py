from django import forms
from aplicacion.models import Usuario

class LoginForm(forms.Form):
	username = forms.CharField(required=True)
	password = forms.CharField(widget=forms.PasswordInput())
	
class RegisterForm(forms.Form):
	username = forms.CharField(required=True)
	first_name = forms.CharField(required=True)
	last_name = forms.CharField(required=True)
	password1 = forms.CharField(widget=forms.PasswordInput(), required=True)
	password2 = forms.CharField(widget=forms.PasswordInput(), required=True)
	fecha_nacimiento = forms.DateField(widget=forms.DateInput(), required=True)
	email = forms.EmailField(required=True)
	telefono = forms.CharField()
	