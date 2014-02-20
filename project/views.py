from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
	"""
	Displays the home page.
	"""
	return render_to_response('home.html', context_instance=RequestContext(request))

def about(request):
	"""
	Displays the 'About' page.
	"""
	return render_to_response('about.html', context_instance=RequestContext(request))

def terms(request):
	"""
	Displays the 'Terms of Use' page.
	"""
	return render_to_response('terms.html', context_instance=RequestContext(request))
