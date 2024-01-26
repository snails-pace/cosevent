import django.core.validators
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext as _


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

def validate_price(self):
    raise ValidationError("bla")

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
    availability = models.PositiveIntegerField(_("No. of tickets available"))
    price = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    artist = models.ForeignKey(Profile, on_delete=models.CASCADE)
    video = models.OneToOneField(Video, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name



    class Meta:
        ordering = ['date']



class Order(models.Model):
    """
    Order Model with automatic add date of instance creation
    """

    customer_name = models.CharField(max_length=255)
    customer_email = models.EmailField()
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        ordering = ['id']


class EventOrder(models.Model):
    """
    EventOrder Model with reference to the Order model to which it belongs
    """

    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    ticket_count = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.id