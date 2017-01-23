from django.contrib.auth.models import User
from django import forms

class UserFrom(forms.ModelFrom):

	password = forms.CharField(widget=forms.PasswordInput)

	class Meta:
		model = User
		filds = ['username', 'email', 'password']