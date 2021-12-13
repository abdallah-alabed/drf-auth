from django.db.models import fields
from django.db.models.base import Model
from rest_framework import serializers
from .models import Movie


class MovieSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['title', 'description', 'rating', 'director', 'release','author']
        model = Movie