from django.db import models
from time import time
from random import choice

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

class Food(models.Model):
    category_choices = (
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

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, choices=category_choices, default='Other')
    restaurant = models.CharField(max_length=50)
    food_type = models.CharField(max_length=50, null=True, blank=True)
    rating = MinMaxFloat(max_value=5.0, min_value=0.0, default=3.0)
    thumbnail = models.FileField(upload_to=get_upload_file_name, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def RandomFood():
    return choice(Food.objects.all())
