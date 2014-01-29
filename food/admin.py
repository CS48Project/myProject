from django.contrib import admin
from food.models import Food, Category

# Register your models here.
class FoodAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	list_display = ('name', 'category', 'restaurant')
	search_fields = ['name']

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Food, FoodAdmin)
admin.site.register(Category, CategoryAdmin)
