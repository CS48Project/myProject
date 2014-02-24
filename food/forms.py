"""
Form classes
"""

from django import forms
from django.forms import ModelForm
from food.models import *

class FoodForm(ModelForm):
	"""
	A form that creates a Food object from the given information.
	"""

	# Define the form's fields and their properties.
	name = forms.CharField(max_length=50)
	category = forms.ModelChoiceField(queryset=Category.objects.order_by('name'),
                                      empty_label="Pick a category")
	restaurant = forms.ModelChoiceField(queryset=Restaurant.objects.order_by('name'),
										empty_label="Pick a restaurant")
	price = forms.DecimalField(min_value=0, max_digits=5, decimal_places=2, required=False)
	picture = forms.FileField(required=False)

	# Model the form after the Food class, and indicate the form fields to be shown.
	class Meta:
		model = Food
		fields = ['name', 'category', 'restaurant', 'price', 'picture']
