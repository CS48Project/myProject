from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from food.forms import FoodForm
from food.models import *

# Create your views here.
@login_required
def submit(request):
  if request.method == 'POST':
    form = FoodForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/food/submitsuccess/')
  else:
    form = FoodForm()
  args = {}
  args.update(csrf(request))
  args['form'] = form
  return render_to_response('submit.html', args,
                            context_instance=RequestContext(request))

def food_index(request):
  food_index = Food.objects.order_by('name')
  context = {'food_index': food_index}
  return render_to_response('food_index.html', context,
                            context_instance=RequestContext(request))

def food(request, categoryslug, foodslug, food_id):
  food = Food.objects.get(id=food_id)
  context = {'food': food}
  return render_to_response('food.html', context,
                            context_instance=RequestContext(request))

def what_to_eat(request):
  random_food = RandomFood()
  context = {'random_food': random_food}
  return render_to_response('what_to_eat.html', context,
                            context_instance=RequestContext(request))

def food_of_the_day(request):
  return render_to_response('food_of_the_day.html',
                            context_instance=RequestContext(request))

def category_index(request):
  category_index = Category.objects.order_by('name')
  context = {'category_index': category_index}
  return render_to_response('category_index.html', context,
                            context_instance=RequestContext(request))

def category(request, categoryslug):
  category = Category.objects.get(slug=categoryslug)
  food_list = Food.objects.filter(category=category).order_by('name')
  context = {'category': category, 'food_list': food_list}
  return render_to_response('category.html', context,
                            context_instance=RequestContext(request))

def submit_success(request):
  return render_to_response('submit_success.html',
                            context_instance=RequestContext(request))
