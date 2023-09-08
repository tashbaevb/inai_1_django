from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=155)
    description = models.TextField(null=True)
    image = models.ImageField()
    genre = models.CharField(max_length=200)
    duration = models.IntegerField(null=True)
    country = models.CharField(max_length=400)

