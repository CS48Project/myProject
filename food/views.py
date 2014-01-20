from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.context_processors import csrf
from food.forms import FoodForm
from food.models import Food, Category, RandomFood

# Create your views here.
def submit(request):
    if request.POST:
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/food/')
    else:
      form = FoodForm()
    args = {}
    args.update(csrf(request))
    args['form'] = form
    return render_to_response('submit.html', args, context_instance=RequestContext(request))

def food_index(request):
    return render_to_response('food_index.html', {'food_index': Food.objects.all()},
                              context_instance=RequestContext(request))

def food(request, food_id=1):
    return render_to_response('food.html', {'food': Food.objects.get(id=food_id)},
                              context_instance=RequestContext(request))

def what_to_eat(request):
    return render_to_response('what_to_eat.html', {'random_food': RandomFood()},
                              context_instance=RequestContext(request))

def food_of_the_day(request):
    return render_to_response('food_of_the_day.html',
                              context_instance=RequestContext(request))

def category_index(request):
    return render_to_response('category_index.html',
                             {'category_index': Category.objects.all()},
                              context_instance=RequestContext(request))

def category(request):
    return render_to_response('category.html',
                             {'category': Category.objects.get(id=category_id)},
                              context_instance=RequestContext(request))
