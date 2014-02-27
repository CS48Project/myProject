"""
Views associated with the 'food' app
"""

from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from food.forms import FoodForm, SearchForm
from food.models import *

# Create your views here.
@login_required
def submit(request):
  """
  Displays the food submit form and handles the food creation action.
  Requires user to be logged in.
  """
  if request.method == 'POST':
    form = FoodForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect('/food/submitsuccess/')
  else:
    """User is not submitting form, show them a black submission form."""
    form = FoodForm()
  context = {'form': form}
  context.update(csrf(request))
  return render_to_response('submit.html', context,
                            context_instance=RequestContext(request))

@login_required
def edit(request, foodslug, food_id):
  """
  Displays the food edit form and handles the food edit info action.
  Requires user to be logged in.
  """
  food = Food.objects.get(id=food_id)
  if request.method == 'POST':
    form = FoodForm(request.POST, request.FILES, instance=food)
    if form.is_valid():
      form.save()
      return HttpResponseRedirect(food.get_absolute_url())
  else:
    """User is not submitting form, show them a black edit form."""
    form = FoodForm(instance=food)
  context = {'form': form}
  context.update(csrf(request))
  return render_to_response('edit.html', context,
                            context_instance=RequestContext(request))

def food_index(request):
  """
  Displays a list of all Food objects.
  """
  food_index = Food.objects.order_by('name')
  context = {'food_index': food_index}
  context.update(csrf(request))
  return render_to_response('food_index.html', context,
                            context_instance=RequestContext(request))

def food(request, foodslug, food_id):
  """
  Displays the details of a specific Food object.
  """
  food = Food.objects.get(id=food_id)
  context = {'food': food}
  return render_to_response('food.html', context,
                            context_instance=RequestContext(request))

def what_to_eat(request):
  """
  Displays the random Food object generated by the RandomFood() helper
  function.
  """
  random_food = RandomFood()
  context = {'random_food': random_food}
  return render_to_response('what_to_eat.html', context,
                            context_instance=RequestContext(request))

def food_of_the_day(request):
  """
  Displays the most popular Food object.
  """
  return render_to_response('food_of_the_day.html',
                            context_instance=RequestContext(request))

def category_index(request):
  """
  Displays a list of all Category objects.
  """
  category_index = Category.objects.order_by('name')
  context = {'category_index': category_index}
  return render_to_response('category_index.html', context,
                            context_instance=RequestContext(request))

def category(request, categoryslug):
  """
  Displays a list of all Food objects with the specified Category.
  """
  category = Category.objects.get(slug=categoryslug)
  food_list = Food.objects.filter(category=category).order_by('name')
  context = {'category': category, 'food_list': food_list}
  return render_to_response('category.html', context,
                            context_instance=RequestContext(request))

def restaurant_index(request):
  """
  Displays a list of all Restaurant objects.
  """
  restaurant_index = Restaurant.objects.order_by('name')
  context = {'restaurant_index': restaurant_index}
  return render_to_response('restaurant_index.html', context,
                            context_instance=RequestContext(request))

def restaurant(request, restaurantslug):
  """
  Displays a list of Food objects with the specified Restaurant.
  """
  restaurant = Restaurant.objects.get(slug=restaurantslug)
  food_list = Food.objects.filter(restaurant=restaurant).order_by('name')
  context = {'restaurant': restaurant, 'food_list': food_list}
  return render_to_response('restaurant.html', context,
                            context_instance=RequestContext(request))

def submit_success(request):
  """
  Displays a message for the user indicating that the food form has
  been successfully submitted.
  """
  return render_to_response('submit_success.html',
                            context_instance=RequestContext(request))

def search_page(request):
  if request.method == 'POST':
    form = SearchForm(request.POST)
    if form.is_valid():
      name_results = Food.objects.filter(name__contains=form.cleaned_data['text']).order_by('name')
      if form.cleaned_data['has_image']:
        name_results = name_results.exclude(picture='')
      context = {'form': form, 'name_results': name_results}

      if form.cleaned_data['search_category']:
        category_results = Food.objects.filter(category__name__contains=form.cleaned_data['text']).order_by('name')
        if form.cleaned_data['has_image']:
          category_results = category_results.exclude(picture='')
        context['category_results'] = category_results

      if form.cleaned_data['search_restaurant']:
        restaurant_results = Food.objects.filter(restaurant__name__contains=form.cleaned_data['text']).order_by('name')
        if form.cleaned_data['has_image']:
          restaurant_results = restaurant_results.exclude(picture='')
        context['restaurant_results'] = restaurant_results

      return render_to_response('search.html', context,
                                context_instance=RequestContext(request))
    else:
      return render_to_response('search.html', {'form': form},
                                context_instance=RequestContext(request))
  form = SearchForm()
  context = {'form': form}
  return render_to_response('search.html', context,
                            context_instance=RequestContext(request))
