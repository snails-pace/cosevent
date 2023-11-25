from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here

class User(AbstractUser):
    # email and username have to be unique
    # returns username as string representation
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.username


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)


class Category(models.Model):
    # Category model with name as string representation
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Event(models.Model):
    # Category Event with name as string representation
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    availability = models.PositiveIntegerField()
    artist_name = models.CharField(max_length=255)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']

