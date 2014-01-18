from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    return render_to_response('home.html', context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html', context_instance=RequestContext(request))

def terms(request):
    return render_to_response('terms.html', context_instance=RequestContext(request))
