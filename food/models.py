from django.db import models
from time import time
from random import choice

def get_upload_file_name(instance, filename):
    return "uploaded_files/%s_%s" % (str(time()).replace('.','_'), filename)

# Create your models here.
class Food(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    food_type = models.CharField(max_length=100)
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
    food_list = Food.objects.all()
    return choice(food_list)
