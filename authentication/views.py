"""
Views associated with the 'authentication' app
"""

from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from authentication.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout, REDIRECT_FIELD_NAME

# Create your views here.
def UserRegistration(request):
	"""
	Displays the user registration form and handles the user creation action.
	"""
	if request.method == 'POST':
		form = RegistrationForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(username=form.cleaned_data['username'],
											first_name=form.cleaned_data['first_name'],
											last_name=form.cleaned_data['last_name'],
											email=form.cleaned_data['email'],
											password=form.cleaned_data['password'])
			user.save()
			return HttpResponseRedirect('/accounts/registrationsuccess/')
		else:
			return render_to_response('register.html', {'form': form},
									  context_instance=RequestContext(request))
	else:
		"""User is not submitting form, show them a black registration form."""
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html', context,
								  context_instance=RequestContext(request))

def LoginRequest(request, redirect_field_name=REDIRECT_FIELD_NAME):
	"""
	Displays the login form and handles the login action.
	"""
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/profile/')
	redirect_to = request.REQUEST.get(redirect_field_name, '')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			if not form.cleaned_data.get('remember'):
				request.session.set_expiry(0)
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return HttpResponseRedirect(redirect_to)
			else:
				return render_to_response('login.html', {'form': form},
										  context_instance=RequestContext(request))
		else:
			return render_to_response('login.html', {'form': form},
									  context_instance=RequestContext(request))
	else:
		"""User is not submitting form, show them a login form."""
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context,
								  context_instance=RequestContext(request))

def LogoutRequest(request):
	"""
	Logs out the user.
	"""
	logout(request)
	return render_to_response("logoutsuccess.html",
							  context_instance=RequestContext(request))

def registrationsuccess(request):
	"""
	Lets the user know they have successfully created an account.
	"""
	return render_to_response("registrationsuccess.html",
							  context_instance=RequestContext(request))

@login_required
def profile(request):
	"""
	Displays the user's profile information. Requires user to be logged in.
	"""
	return render_to_response("profile.html", context_instance=RequestContext(request))

def all_votes(request):
	return render_to_response("all_votes.html", context_instance=RequestContext(request))
