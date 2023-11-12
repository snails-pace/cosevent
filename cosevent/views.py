from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.views.generic import TemplateView

from cosevent.forms import UpdateEventForm
from cosevent.models import Event


# Create your views here.
class EventListView(generic.ListView):
    model = Event
    context_object_name = 'event_list'
    template_name = 'event_list.html'


class EventView(generic.DetailView):
    model = Event
    context_object_name = 'event'
    template_name = 'event.html'


class UpdateEventView(generic.UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'

    def get_success_url(self):
        return reverse_lazy('event', args=[self.object.pk])
    
    def form_valid(self, form):
        submitted_date = form.cleaned_data
        
        return super().form_valid(form)

