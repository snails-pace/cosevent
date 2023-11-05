from django.db import models


# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(max_length=254, unique=True)
    password = models.CharField(max_length=50)
    artist_name = models.CharField(max_length=100, default="")



class Event(models.Model):
    event_name = models.CharField(max_length=255)
    event_date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    category = models.CharField(max_length=20)
    availability = models.BooleanField(default=False)
    artist_name = models.ForeignKey(User, on_delete=models.PROTECT)

