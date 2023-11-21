from django.contrib import admin
from cosevent import models
from cosevent.models import Event, Category

# Register your models here.


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    # Registering Event to admin with name ordering and 20 entries per page
    list_display = ['id', 'name', 'date', 'venue', 'category_id', 'availability', 'artist_name', 'description']
    list_editable = ['name', 'date', 'venue', 'availability', 'artist_name', 'description']
    ordering = ['name']
    list_per_page = 20


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    # Registering Category to admin with name ordering and 20 entries per page
    list_display = ['id', 'name']
    list_editable = ['name']
    ordering = ['name']
    list_per_page = 20