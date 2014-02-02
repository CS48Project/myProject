from django.db import models
from django.template.defaultfilters import slugify
from random import choice
from ratings.handlers import ratings

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    category = models.ForeignKey('Category')
    restaurant = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    picture = models.FileField(upload_to=get_upload_file_name, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Food, self).save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()

    def __str__(self):
        return self.name

def RandomFood():
    return choice(Food.objects.all())

ratings.register(Food, score_step=0.5)
