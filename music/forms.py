from django.contrib.auth.models import User
from django import forms

class UserForm(Form):
	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		filds = ['username', 'email', 'password']