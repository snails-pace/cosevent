from django.db import models


# Create your models here.
# class User(models.Model):
#     username = models.CharField(max_length=255, unique=True)
#     email = models.EmailField(max_length=254, unique=True)
#     password = models.CharField(max_length=50)
#     artist_name = models.CharField(max_length=100, default="")



class Event(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    category = models.CharField(max_length=255)
    availability = models.PositiveIntegerField()
    artist_name = models.CharField(max_length=255)

