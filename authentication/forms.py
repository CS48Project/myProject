"""
Form classes
"""

from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm

class RegistrationForm(ModelForm):
	"""
	A form that creates a user, with no privileges, from the given information.
	"""

	# Define the form's fields and their properties.
	username = forms.CharField(max_length=50)
	first_name = forms.CharField(max_length=50)
	last_name = forms.CharField(max_length=50)
	email = forms.EmailField()
	password = forms.CharField(max_length=50,
							   widget=forms.PasswordInput(render_value=False))
	password1 = forms.CharField(max_length=50,
								widget=forms.PasswordInput(render_value=False))
	agree = forms.BooleanField(error_messages={'required': 'You must agree to the Terms of Use.'})

	# Model the form after the default Django User class, and indicate the form fields to be shown.
	class Meta:
		model = User
		fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password1',
				  'agree']

	def clean_username(self):
		"""
		Check to see if the username already exists. If it does, raise a validation error.
		Otherwise, create the user.
		"""
		username = self.cleaned_data['username']
		try:
			User.objects.get(username=username)
		except User.DoesNotExist:
			return username
		raise forms.ValidationError("That username is already taken. "
									"Please select another.")

	def clean_password1(self):
		"""
		Check to make sure the passwords match.
		"""
		if 'password' in self.cleaned_data:
			password = self.cleaned_data['password']
			password1 = self.cleaned_data['password1']
		if password == password1:
			return password1
		raise forms.ValidationError("The passwords you entered did not match. "
									"Please try again.")

class LoginForm(forms.Form):
	"""
	A form that handles the authentication of existing users.
	"""

	# Define the form's fields and their properties.
	username = forms.CharField(max_length=50)
	password = forms.CharField(max_length=50,
							   widget=forms.PasswordInput(render_value=False))
	remember = forms.BooleanField(required=False)
