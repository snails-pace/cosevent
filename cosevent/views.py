from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
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


class UpdateEventView(SuccessMessageMixin, generic.UpdateView):
    model = Event
    form_class = UpdateEventForm
    template_name = 'update_event.html'
    success_message = 'Your event %(name)s was saved'

    def get_success_url(self):
        return reverse_lazy('event', args=[self.object.pk])
    
    def form_valid(self, form):
        submitted_date = form.cleaned_data
        
        return super().form_valid(form)


# class CreateEventView(SuccessMessageMixin, generic.CreateView):
#     model = Event
#     form_class = UpdateEventForm
#     template_name = 'create_event.html'
#     success_message = 'Your event %(name)s was saved'
#
#     def get_success_url(self):
#         return reverse_lazy('event', args=[self.object.pk])
#
#     def form_valid(self, form):
#         submitted_date = form.cleaned_data
#
#         return super().form_valid(form)


class DeleteEventView(SuccessMessageMixin, generic.DeleteView):
    model = Event
    context_object_name = 'event'
    template_name = 'delete_event.html'
    success_url = reverse_lazy('event_list')
    success_message = 'Event deleted'


def create_event_view(request):
    if request.method == 'POST':
        event_form = UpdateEventForm(request.POST)
        if event_form.is_valid():
            event_form.save()
            return redirect('event_list')

    else:
        event_form = UpdateEventForm()

    context = {'form': event_form}
    context['title'] = 'Create Event'
    return render(request, 'create_event.html', context)