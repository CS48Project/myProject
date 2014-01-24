from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegistrationForm(ModelForm):
	username = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField()
	password = forms.CharField(widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password1']

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken. "
									"Please select another.")

	def clean_password1(self):
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			password1 = self.cleaned_data['password1']
		if password == password1:
			return password1
		raise forms.ValidationError("The passwords you entered did not match. "
									"Please try again.")

class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50,
							   widget=forms.PasswordInput(render_value=False))
