from django import forms
from django.forms import ModelForm
from food.models import Food

class FoodForm(ModelForm):
	category_choices = (
		('', 'Pick a category'),
        ('American', 'American'),
        ('Asian', 'Asian'),
        ('Barbecue', 'Barbecue'),
        ('Breakfast, Brunch & Lunch', 'Breakfast, Brunch & Lunch'),
        ('Chinese', 'Chinese'),
        ('Dessert', 'Dessert'),
        ('Fast Food', 'Fast Food'),
        ('French', 'French'),
        ('Hamburgers & Hot Dogs', 'Hamburgers & Hot Dogs'),
        ('Health Food', 'Health Food'),
        ('Ice Cream & Frozen Desserts', 'Ice Cream & Frozen Desserts'),
        ('Indian', 'Indian'),
        ('Italian', 'Italian'),
        ('Japanese', 'Japanese'),
        ('Mexican', 'Mexican'),
        ('Other', 'Other'),
        ('Pizza', 'Pizza'),
        ('Sandwich Shops', 'Sandwich Shops'),
        ('Seafood', 'Seafood'),
        ('Steak Houses', 'Steak Houses'),
        ('Thai', 'Thai'),
        ('Vietnamese', 'Vietnamese'),
    )

	name = forms.CharField(max_length=50)
	category = forms.ChoiceField(choices=category_choices)
	restaurant = forms.CharField(max_length=50)
	price = forms.DecimalField(min_value=0, max_digits=5, decimal_places=2)
	rating = forms.DecimalField(min_value=0, max_value=5, max_digits=2,
								decimal_places=1, required=False)
	picture = forms.FileField(required=False)

	class Meta:
		model = Food
		fields = ['name', 'category', 'restaurant', 'price', 'rating', 'picture']
