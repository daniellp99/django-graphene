from django.contrib import admin

from ingredients.models import Category, Ingredient

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Category)
