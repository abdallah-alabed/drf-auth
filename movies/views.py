from django.shortcuts import render
from rest_framework import generics
from .serializers import MovieSerialzer
from .models import Movie

# CR views
class MovieList(generics.ListCreateAPIView):
    # queryset = Movie.objects.filter(published = True)
    queryset = Movie.objects.all()
    serializer_class = MovieSerialzer

# RUD view
class MovieDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerialzer