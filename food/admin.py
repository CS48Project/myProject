"""
Defines behavior of 'food' models within the admin backend
"""

from django.contrib import admin
from food.models import Food, Category

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'category', 'restaurant')
	search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

# Register the Food and Category models with the admin backend.
admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
