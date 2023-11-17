from django.db import models


# Create your models here


class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    availability = models.PositiveIntegerField()
    artist_name = models.CharField(max_length=255)


class Category(models.Model):
    name = models.CharField(max_length=255)

