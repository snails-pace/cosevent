from django.shortcuts import render
from django.views import generic
from django.views.generic import TemplateView

from cosevent.models import Event


# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'

class EventView(TemplateView):
    template_name = "event.html"
