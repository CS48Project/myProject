from django.db import models
from time import time
from random import choice

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Food(models.Model):
    category_choices = (
        ('Am', 'American'),
        ('As', 'Asian'),
        ('BBQ', 'Barbecue'),
        ('BBL', 'Breakfast, Brunch & Lunch'),
        ('Ch', 'Chinese'),
        ('De', 'Dessert'),
        ('FF', 'Fast Food'),
        ('Fr', 'French'),
        ('HHD', 'Hamburgers & Hot Dogs'),
        ('HF', 'Health Food'),
        ('ICFD', 'Ice Cream & Frozen Desserts'),
        ('In', 'Indian'),
        ('It', 'Italian'),
        ('Ja', 'Japanese'),
        ('Mx', 'Mexican'),
        ('Mi', 'Miscellaneous'),
        ('Pz', 'Pizza'),
        ('SS', 'Sandwich Shops'),
        ('Se', 'Seafood'),
        ('SH', 'Steak Houses'),
        ('Th', 'Thai'),
        ('Vi', 'Vietnamese'),
    )

    food_type_choices = (
        ('Mi', 'Miscellaneous'),
    )

    name = models.CharField(max_length=50)
    category = models.CharField(max_length=4, choices=category_choices, default='Mi')
    food_type = models.CharField(max_length=4, choices=food_type_choices, default='Mi')
    rating = models.IntegerField(default=0)
    thumbnail = models.FileField(upload_to=get_upload_file_name)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=100)
    url_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

def RandomFood():
    return choice(Food.objects.all())
