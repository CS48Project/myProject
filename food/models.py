"""
Models (classes) associated with the 'food' app
"""

from django.db import models
from django.template.defaultfilters import slugify
from random import choice
from ratings.handlers import ratings
from ratings.forms import StarVoteForm

def get_upload_file_name(instance, filename):
    """
    Helper function that creates the uploaded file in the uploaded_files directory
    in order to be served as a static file on the site.
    """
    return "uploaded_files/%s" % (filename)

# Create your models here.
class Food(models.Model):
    """
    Defines the state and behavior of a Food object.
    """
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ForeignKey('Category')
    restaurant = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    picture = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)

    # Automatically slugifies the Food object's name upon creation.
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)

    # Returns the Food object's URL.
    def get_absolute_url(self):
        return "/food/categories/" + str(self.category.slug) + "/" + str(self.slug) + "/" + str(self.id) + "/"
    
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

    # Returns the Category object's URL.
    def get_absolute_url(self):
        return "/food/categories/" + str(self.slug) + "/"

    # Define the unicode version of a Category object.
    def __str__(self):
        return self.name

def RandomFood():
    """
    Helper function that returns a random Food object from the database.
    """
    return choice(Food.objects.all())

# Register the Food class in order to be used with the 'ratings' app.
ratings.register(Food, score_range=(0.5, 5), score_step=0.5, form_class=StarVoteForm)
