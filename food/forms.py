from django import forms
from django.forms import ModelForm
from food.models import Food, Category

class FoodForm(ModelForm):
	name = forms.CharField(max_length=50)
	category = forms.ModelChoiceField(queryset=Category.objects.order_by('name'),
                                      empty_label="Pick a category")
	restaurant = forms.CharField(max_length=50)
	price = forms.DecimalField(min_value=0, max_digits=5, decimal_places=2)
	picture = forms.FileField(required=False)

	class Meta:
		model = Food
		fields = ['name', 'category', 'restaurant', 'price', 'picture']
