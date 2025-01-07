from django.contrib import admin

# Register your models here.
from .models import BlogPost, Category

admin.site.register(BlogPost) # Register the BlogPost model
admin.site.register(Category) # Register the Category model