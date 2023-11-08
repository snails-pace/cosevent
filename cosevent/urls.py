from django.urls import path
from . import views

urlpatterns = [
    path("", views.EventListView.as_view(), name="event_list"),
    path("event/<int:pk>", views.EventView.as_view(), name="event")
    ]
