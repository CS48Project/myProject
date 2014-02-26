"""
Models (classes) associated with the 'food' app
"""

from django.db import models
from django.template.defaultfilters import slugify
from random import choice
from ratings.handlers import ratings
from ratings.forms import StarVoteForm

# Create your models here.
class Food(models.Model):
    """
    Defines the state and behavior of a Food object.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ForeignKey('Category')
    restaurant = models.ForeignKey('Restaurant')
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    picture = models.FileField(upload_to="uploaded_files/food_pics", blank=True, null=True)

    # Automatically slugifies the Food object's name upon creation.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    # Returns the Food object's URL.
    def get_absolute_url(self):
        return "/food/" + str(self.slug) + "/" + str(self.id) + "/"
    
    # Define the unicode version of a Food object.
    def __str__(self):
        return self.name

class Category(models.Model):
    """
    Defines the state and behavior of a Category object. Users will not be able to
    directly create a Category object; they will only be able to select a Food
    object's category on the food submit form.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    picture = models.FileField(upload_to="uploaded_files/category_pics", blank=True, null=True)

    # Returns the Category object's URL.
    def get_absolute_url(self):
        return "/food/categories/" + str(self.slug) + "/"

    # Define the unicode version of a Category object.
    def __str__(self):
        return self.name

class Restaurant(models.Model):
    """
    Defines the state and behavior of a Restaurant object. Users will not be able to
    directly create a Restaurant object; they will only be able to select a Food
    object's restaurant on the food submit form.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    picture = models.FileField(upload_to="uploaded_files/restaurant_pics", blank=True, null=True)

    # Returns the Restaurant object's URL.
    def get_absolute_url(self):
        return "/food/restaurants/" + str(self.slug) + "/"

    # Define the unicode version of a Restaurant object.
    def __str__(self):
        return self.name

def RandomFood():
    """
    Helper function that returns a random Food object from the database.
    """
    return choice(Food.objects.all())

# Register the Food class in order to be used with the 'ratings' app.
ratings.register(Food, score_range=(0.5, 5), score_step=0.5, form_class=StarVoteForm)
