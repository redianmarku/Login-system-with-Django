from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Register(UserCreationForm):
	first_name = forms.CharField(max_length=200, help_text='Put your name here.')
	first_name = forms.CharField(max_length=200, help_text='Put your last name here.')
	email = forms.EmailField(max_length=200, help_text='Put your email here.')

	class Meta:
		fields = (
			'username','first_name', 'last_name',  'email', 'password1'
		)
		model = User

		widget = {
			'username': forms.TextInput(attrs={'class': 'validate', 'id':'username' ,'placeholder': 'Username'}),
			'first_name': forms.TextInput(attrs={'class': 'validate', 'id':'first_name', 'placeholder': 'First Name'}),
			'last_name': forms.TextInput(attrs={'class': 'validate', 'id':'last_name', 'placeholder': 'Last Name'}),
			'email': forms.EmailInput(attrs={'class': 'validate', 'id':'email', 'placeholder': 'Email'}),
			'password1': forms.PasswordInput(attrs={'class': 'validate', 'id':'password', 'placeholder': 'Password'})
	 
		}

	

			


class Login(forms.Form):
	username = forms.CharField(max_length=200, help_text='Put your username here.')
	password = forms.CharField(widget=forms.PasswordInput(), help_text='Put your password here.')

	class Meta:
		fields = (
			'username', 'password'
		)

		model = User