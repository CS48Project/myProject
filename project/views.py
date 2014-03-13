"""
Site-wide views
"""

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import settings

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

def google_analytics(request):
    """
    Use the variables returned in this function to
    render your Google Analytics tracking code template.
    """
    ga_prop_id = getattr(settings, 'GOOGLE_ANALYTICS_PROPERTY_ID', False)
    ga_domain = getattr(settings, 'GOOGLE_ANALYTICS_DOMAIN', False)
    if not settings.DEBUG and ga_prop_id and ga_domain:
        return {
            'GOOGLE_ANALYTICS_PROPERTY_ID': ga_prop_id,
            'GOOGLE_ANALYTICS_DOMAIN': ga_domain,
        }
    return {}
