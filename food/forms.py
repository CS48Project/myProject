from django import forms
from django.forms import ModelForm
from food.models import Food

class FoodForm(ModelForm):

    class Meta:
        model = Food
        fields = ['name', 'category', 'food_type', 'rating', 'thumbnail']
