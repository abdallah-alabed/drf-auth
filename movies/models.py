from django.db import models
from django.contrib.auth import get_user_model


class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    rating = models.IntegerField()
    director = models.CharField(max_length=255)
    release = models.DateTimeField(auto_now = False, auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.title