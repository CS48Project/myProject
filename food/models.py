from django.db import models
from django.template.defaultfilters import slugify
from random import choice

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey('Category')
    restaurant = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    picture = models.FileField(upload_to=get_upload_file_name)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

def RandomFood():
    return choice(Food.objects.all())
