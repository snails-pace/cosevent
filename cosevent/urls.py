from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("event/<int:pk>", views.EventView.as_view(), name="event"),
    path("event/<int:pk>/update", views.UpdateEventView.as_view(), name="update_event"),
    path("event/create", views.create_event_view, name="create_event"),
    path("event/<int:pk>/delete", views.DeleteEventView.as_view(), name="delete_event"),
    path("categories", views.category_list_view, name="category_list"),
    path("category/create", views.create_category_view, name="category_create"),
    path("category/<int:pk>/delete", views.category_delete_view, name="category_delete")
    ]
