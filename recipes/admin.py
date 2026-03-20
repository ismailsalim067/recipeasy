from django.contrib import admin
from .models import Rating, Recipes

admin.site.register(Recipes)
admin.site.register(Rating)

# Register your models here.
