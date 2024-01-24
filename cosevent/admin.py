from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from cosevent import models
from cosevent.models import Event, Category, User, Profile


# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    """Registering Event to admin with name ordering and 10 entries per page"""

    list_display = ['id', 'name', 'date', 'venue', 'category_id', 'availability', 'artist', 'description', 'video']
    list_editable = ['name', 'date', 'venue', 'availability', 'artist', 'description', 'video']
    ordering = ['name']
    list_per_page = 10



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Registering Category to admin with name ordering and 10 entries per page"""

    list_display = ['id', 'name']
    list_editable = ['name']
    ordering = ['name']
    list_per_page = 10


@admin.register(User)
class UserAdmin(UserAdmin):
    """Registering User to admin with email ordering and 10 entries per page"""

    ordering = ['email']
    list_per_page = 10


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Registering Profile to admin with nickname ordering and 10 entries per page"""

    list_display = ['id', 'nickname', 'birthdate']
    list_editable = ['nickname', 'birthdate']
    ordering = ['nickname']
    list_per_page = 10


@admin.register(models.Video)
class VideoAdmin(admin.ModelAdmin):
    """Registering Video to admin with id ordering and 10 entries per page"""
    list_display = ['id', 'title', 'video_url']
    list_editable = ['title', 'video_url']
    ordering = ['id']
    list_per_page = 10

