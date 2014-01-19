from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentication.models import Wallaby

class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User name'))
	first_name = forms.CharField(label=(u'First name'))
	last_name = forms.CharField(label=(u'Last name'))
	email = forms.EmailField(label=(u'Email'))
	password = forms.CharField(label=(u'Password'),
							   widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify password'),
							    widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = Wallaby
		fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password1', 'birthday']

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
		raise forms.ValidationError("The passwords you entered do not match.")

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User name'))
	password = forms.CharField(label=(u'Password'),
							   widget=forms.PasswordInput(render_value=False))
