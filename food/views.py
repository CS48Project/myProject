from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from food.forms import FoodForm
from food.models import Food

# Create your views here.
def create(request):
    if request.POST:
        form = FoodForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            
            return HttpResponseRedirect('/food/all/')
        else:
            form = FoodForm()

        args = {}
        args.update(csrf(request))

        args['form'] = form

        return render_to_response('submit.html', args)

def food_index(request):
    return render_to_response('food_index.html', {'food_index': Food.objects.all()})

def food(request, food_id=1):
    return render_to_response('food.html', {'food': Food.objects.get(id=food_id)})
