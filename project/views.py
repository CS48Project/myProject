from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import render_to_response
from django.template import RequestContext

# Create your views here.
def home(request):
    return render_to_response('home.html')

def what_to_eat(request):
    return render_to_response('what_to_eat.html')

def food_of_the_day(request):
    return render_to_response('food_of_the_day.html')

def submit(request):
    return render_to_response('submit.html')

def index(request):
    return render_to_response('index.html')

def terms(request):
    return render_to_response('terms.html')
