from django.shortcuts import render
from django.views import generic

from cosevent.models import Event


# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'


