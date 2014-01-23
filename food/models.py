from django.db import models
from random import choice

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s" % (filename)

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    restaurant = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    likes = models.IntegerField(default=0)
    picture = models.FileField(upload_to=get_upload_file_name)
    
    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50)
    url_name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

def RandomFood():
    return choice(Food.objects.all())
