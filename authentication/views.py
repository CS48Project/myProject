from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from authentication.forms import RegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import REDIRECT_FIELD_NAME

# Create your views here.
def UserRegistration(request):
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
		''' user is not submitting form, show them black registration form '''
		form = RegistrationForm()
		context = {'form': form}
		return render_to_response('register.html', context,
								  context_instance=RequestContext(request))

def LoginRequest(request, redirect_field_name=REDIRECT_FIELD_NAME):
	if request.user.is_authenticated():
		return HttpResponseRedirect('/accounts/profile/')
	redirect_to = request.REQUEST.get(redirect_field_name, '')
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
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
		''' user is not submitting form, show login form '''
		form = LoginForm()
		context = {'form': form}
		return render_to_response('login.html', context,
								  context_instance=RequestContext(request))

def LogoutRequest(request):
	logout(request)
	return render_to_response("logoutsuccess.html",
							  context_instance=RequestContext(request))

def registrationsuccess(request):
	return render_to_response("registrationsuccess.html",
							  context_instance=RequestContext(request))

@login_required
def profile(request):
	return render_to_response("profile.html", context_instance=RequestContext(request))
