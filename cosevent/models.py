from django.db import models


# Create your models here

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Event(models.Model):

    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    availability = models.PositiveIntegerField()
    artist_name = models.CharField(max_length=255)




