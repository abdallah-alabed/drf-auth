from django.contrib import admin
from .models import Movie


@admin.register(Movie)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'rating', 'director', 'release']