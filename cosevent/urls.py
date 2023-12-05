from django.urls import path
from . import views

urlpatterns = [
    path("", views.event_list_view, name="event_list"),
    path("my_events", views.my_event_list_view, name="my_events"),
    path("event/<int:pk>", views.event_view, name="event"),
    path("event/<int:pk>/update", views.update_event_view, name="event_update"),
    path("event/create", views.create_event_view, name="event_create"),
    path("event/<int:pk>/delete", views.event_delete_view, name="event_delete"),
    path("categories", views.category_list_view, name="category_list"),
    path("category/create", views.create_category_view, name="category_create"),
    path("category/<int:pk>/delete", views.category_delete_view, name="category_delete")
    ]
