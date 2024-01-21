from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here

class User(AbstractUser):
    """
    User model with username as string representation
    Takes email instead of username for login
    Fields email and username have to be unique
    """

    email = models.EmailField(unique=True)
    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.username


class Profile(models.Model):
    """
    Profile model with nickname as string representation
    References the User model in the user field
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=255)
    birthdate = models.DateField(null=True)

    def __str__(self):
        return self.nickname


class Category(models.Model):
    """
    Category model with name field as string representation
    Ordering by name field
    """

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Video(models.Model):
    """ Video model with title as string representation """
    title = models.CharField(max_length=255)
    video_url = models.URLField()

    def __str__(self):
        return self.title


class Event(models.Model):
    """
    Event model with name as string representation
    Ordering by date
    """

    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True)
    venue = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    availability = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    artist = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.OneToOneField(Video, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['date']



