from django.db import models


# Create your models here

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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

