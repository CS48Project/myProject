from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from authentication.models import Wallaby

class RegistrationForm(ModelForm):
	username = forms.CharField(label=(u'User name'))
	email = forms.EmailField(label=(u'Email'))
	password = forms.CharField(label=(u'Password'),
							   widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(label=(u'Verify password'),
							    widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = Wallaby
		exclude = ('user',)

	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken. "
									"Please select another.")

	def clean(self):
		if self.cleaned_data['password'] != self.cleaned_data['password1']:
			raise forms.ValidationError("The passwords did not match. "
										"Please try again.")
		return self.cleaned_data

class LoginForm(forms.Form):
	username = forms.CharField(label=(u'User name'))
	password = forms.CharField(label=(u'Password'),
							   widget=forms.PasswordInput(render_value=False))
