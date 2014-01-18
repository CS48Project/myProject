from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

# Create your models here.
class Wallaby(models.Model):
	user = models.OneToOneField(User)
	name = models.CharField(max_length=100)
	birthday = models.DateField()

	def __str__(self):
		return self.name
